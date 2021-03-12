from cmd import Cmd
import six
import pyfiglet
import urllib3
import requests
import click
from datetime import date
import csv
import os
import json
import jwt
from pathlib import Path

base_url = "https://localhost:8765/evcharge/ap"

@click.group()
def main():
	pass

def tokenizer(filename):
    if os.path.exists(filename):
        filereader = open(filename, 'r')
        Data = filereader.readline()
        filereader.close()
        token = str(Data[11:len(Data)-2])
        return {"Token":token}
    else:
        click.echo("You need to login for this action")
        return None

def errorhandling(r):
    if r.status_code == 400:
        click.echo(str(r.status_code)+ ": Bad request")
        return False
    elif r.status_code == 401:
        click.echo(str(r.status_code)+ ": Not authorized")
        return False
    elif r.status_code == 402:
        click.echo(str(r.status_code)+ ": No data")
        return False
    elif r.status_code == 200:
        return True
    else:
        click.echo("Other status code: "+ str(r.status_code))
        return False

def dateresolver(date):
    if len(date) == 10:
        return "date/" + date
    elif len(date) == 7:
        return "month/" + date
    elif len(date) == 4:
        return "year/" + date
    return ""


@click.option('--passw', prompt='Your password',hide_input=True, help='The password of the User')
@click.option('--username', prompt='Your username', help='The username of the User')
@main.command()
def login(username, passw):
    url = base_url + "/Login"
    filename = home + "/softeng20bAPI.token"
    r = requests.post(url, json.dumps({'username': username, 'password':passw }))
    if errorhandling(r):
        if len(r.text)<100:
            click.echo(r.text)
        else:
            file = open(filename, 'w')
            file.write(r.text)
            file.close()
            log("The Charging Aces")
            log("Welcome to e-λέκτρα CLI app!")
            click.echo('Hello %s!' % username)



@main.command()
def logout():
    url = base_url + "/Logout"
    filename = home + "/softeng20bAPI.token"
    token = tokenizer(filename)
    if token != None:
        r = requests.post(url, headers=token)
        if errorhandling(r):
            os.remove(filename)
            click.echo('You have logged out. Goodbye!')

@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@click.option('--datefrom', prompt='Please enter the starting date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--dateto', prompt='Please enter the ending date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--point', prompt='Please enter the point name', help='Name of Point')
@main.command()
def SessionsPerPoint(point, datefrom, dateto, format):
    url = base_url + "/SessionsPerPoint/" + point + "/" + dateresolver(datefrom) + "/" + dateresolver(dateto) + '?format=' + format
    filename = home + "/softeng20bAPI.token"
    newfile = home + "/SessionsPerPoint_" + point + "_" + dateresolver(datefrom).replace('/','_') +  "_" + dateresolver(dateto).replace('/', '_') + '.' + format
    token = tokenizer(filename)
    #print(token)
    if token!=None:
        r = requests.get(url, headers = token)
        if errorhandling(r):
            with open(newfile, 'w') as new:
                if format == 'json':
                    json.dump(r.json(), new)
                else:
                    new.write(r.content.decode("UTF-8"))
            click.echo("Data downloaded at " + newfile)
            
            
cli = click.CommandCollection(sources = [main])

if __name__ == '__main__':
     cli()

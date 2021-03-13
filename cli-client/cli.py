# e-Lectra Project by The Charging Aces:
# ~Stelios Kandylakis
# ~Margarita   Oikonomakou
# ~Kitsos      Orfanopoulos
# ~Vasilis     Papalexis
# ~Georgia     Stamou
# ~Dido        Stoikou
# Softeng, ECE NTUA, 2021

# cli code

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

base_url = "https://localhost:8765/evcharge/api"

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


@main.command()
@click.option('--format')
@click.option('--apikey')
def healthcheck(format,apikey):
    #url='https://localhost:8765/evcharge/api/healthcheck'
    response = requests.get(url=url)
    if format=="json":
        print(response.json())
    else:
        if response.status_code != 200:
            print('Failed to get data:', response.status_code)
        else:
            wrapper = csv.reader(response.text.strip().split('\n'))
            for record in wrapper:
                print(record)

@main.command()
@click.option('--format')
@click.option('--apikey')
def resetsessions(format,apikey):
    #url='https://localhost:8765/evcharge/api/resetsessions'
    response = requests.get(url=url)
    if format=="json":
        print(response.json())
    else:
        if response.status_code != 200:
            print('Failed to get data:', response.status_code)
        else:
            wrapper = csv.reader(response.text.strip().split('\n'))
            for record in wrapper:
                print(record)



@main.command()
@click.option('--station')
@click.option('--datefrom')
@click.option('--dateto')
@click.option('--format')
@click.option('--apikey')
def sessionsperstation(station, datefrom, dateto, format, apikey):
    #url='https://localhost:8765/evcharge/api/SessionsPerStation/'+station+'/'+datefrom+'/'+dateto
    url='http://localhost:8000/'+station+'/'+datefrom+'/'+dateto
    print(url)
    response = requests.get(url=url)
    if format=="json":
        print(response.json())
    else:
        if response.status_code != 200:
            print('Failed to get data:', response.status_code)
        else:
            wrapper = csv.reader(response.text.strip().split('\n'))
            for record in wrapper:
                print(record)




@main.command()
@click.option('--ev')
@click.option('--datefrom')
@click.option('--dateto')
@click.option('--format')
@click.option('--apikey')
def sessionsperev(ev, datefrom, dateto, format, apikey):
    #url='https://localhost:8765/evcharge/api/SessionsPerEV/'+ev+'/'+datefrom+'/'+dateto
    url='http://localhost:8000/'+ev+'/'+datefrom+'/'+dateto
    response = requests.get(url=url)
    print(response.url)
    if format =="json":
        print(response.json())
    else:
        if response.status_code != 200:
            print('Failed to get data:', response.status_code)
        else:
            wrapper = csv.reader(response.text.strip().split('\n'))
            for record in wrapper:
                print(record)

@main.command()
@click.option('--provider')
@click.option('--datefrom')
@click.option('--dateto')
@click.option('--format')
@click.option('--apikey')
def sessionsperprovider(provider, datefrom, dateto, format, apikey):
    #url='https://localhost:8765/evcharge/api/SessionsPerProvider/'+provider+'/'+datefrom+'/'+dateto
    url='http://localhost:8000/'+provider+'/'+datefrom+'/'+dateto
    response = requests.get(url=url)
    print(response.url)
    if format =="json":
        print(response.json())
    else:
        if response.status_code != 200:
            print('Failed to get data:', response.status_code)
        else:
            wrapper = csv.reader(response.text.strip().split('\n'))
            for record in wrapper:
                print(record)
		
		

@main.command()
@click.option('--usermod', is_flag=True)
@click.option('--username', is_flag=True)
@click.option('--passw', is_flag=True)
@click.option('--users', is_flag=True)
@click.option('--sessionsupd', is_flag=True)
@click.option('--source', is_flag=True)
@click.option('--healthcheck', is_flag=True)
@click.option('--resetsessions', is_flag=True)
@click.option('--format', is_flag=True)
@click.option('--apikey', is_flag=True)
def admin(usermod, username, passw, users, sessionsupd, format, apikey):
    if usermode:
        if username:
            if passw:
                #{baseURL}/admin/usermod/:username/:password
                url='https://localhost:8765/evcharge/api/admin/usermod/'+username+'/'+passw
                response = requests.get(url=url)
                if format =="json":
                    print(response.json())
                else:
                    if response.status_code != 200:
                        print('Failed to get data:', response.status_code)
                    else:
                        wrapper = csv.reader(response.text.strip().split('\n'))
                        for record in wrapper:
                            print(record)


    elif users:
        url='https://localhost:8765/evcharge/api/admin/usermod/'+username+'/'+passw
        response = requests.get(url=url)
        if format =="json":
            print(response.json())
        else:
            if response.status_code != 200:
                print('Failed to get data:', response.status_code)
            else:
                wrapper = csv.reader(response.text.strip().split('\n'))
                for record in wrapper:
                    print(record)





    elif healthcheck:
        url='https://localhost:8765/evcharge/api/admin/healthcheck'
        response = requests.get(url=url)
        if format=="json":
            print(response.json())
        else:
            if response.status_code != 200:
                print('Failed to get data:', response.status_code)
	     else:
                wrapper = csv.reader(response.text.strip().split('\n'))
                for record in wrapper:
                    print(record)







    elif sessionsupd:
        url='https://localhost:8765/evcharge/api/admin/system/sessionsupd'
        if os.path.exists(source):
                files = {'file': ('source', open(source, 'r'))}
                r = requests.post(url, files = files)
                if errorhandling(r):
                    parsed = json.loads(r.json())
                    print(json.dumps(parsed, indent=2, sort_keys=True))
                    click.echo("Successfully uploaded data")
            else:
                click.echo("You need to provide a source file")


    elif resetsessions:
        url='https://localhost:8765/evcharge/api/admin/resetsessions'
        response = requests.get(url=url)
        if format =="json":
            print(response.json())
        else:
            if response.status_code != 200:
                print('Failed to get data:', response.status_code)
            else:
                wrapper = csv.reader(response.text.strip().split('\n'))
                for record in wrapper:
                    print(record)


cli = click.CommandCollection(sources = [main])

if __name__ == '__main__':
     cli()

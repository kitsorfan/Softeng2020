##############################################################################
#
#     SETUP CONFIGURATION
#
##############################################################################
#
#   $pipenv install click setuptools
#
#   after that we edit setup.py
#
#   $pip install --editable .
#
###############################################################################

import click
import random
import requests
import csv
from cmd import Cmd
import six
import pyfiglet
import urllib3
from requests.auth import HTTPBasicAuth
from datetime import date
import os
import json
import jwt
from pathlib import Path


baseurl="http://localhost:8765/evcharge/api"


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

home = str(Path.home())
base_url = "http://localhost:8765/evcharge/api"

@click.group()
def main():
    pass


@click.option('--passw', prompt='Your password',hide_input=True, help='The password of the User')
@click.option('--username', prompt='Your username', help='The username of the User')
@main.command()
def login(username, passw):
    url = base_url + "/login"
    #url = 'http://localhost:8765/evcharge/api/login?username=kitsorfan&password=secret'
    filename = home + "/softeng20bAPI.token"
    data = {'username':username, 'password':passw}
    #r = requests.post(url, params = params, json.dumps({'username': username, 'password':passw }))
    response = requests.post(url, data = data)
    if errorhandling(response):
        if len(response.text)<100:
            click.echo(response.text)
        else:
            file = open(filename, 'w')
            file.write(response.text)
            file.close()

@main.command()
@click.option('--apikey')
def logout(apikey):
    url = base_url + "/logout"
    filename = home + "/softeng20bAPI.token"
    auth = HTTPBasicAuth('apikey', apikey)
    token = tokenizer(filename)
    r = requests.post(url, headers=token, auth=auth)
    if errorhandling(r):
        os.remove(filename)
        click.echo('You have logged out. Goodbye!')


@click.option('--format', type=click.Choice(['csv', 'json']), default='json' , help='The format with which you want the results to be in')
@click.option('--datefrom', prompt='Please enter the starting date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--dateto', prompt='Please enter the ending date', help='Date in YYYY-MM-DD format, Month in YYYY-MM format or Year in YYYY format')
@click.option('--point', prompt='Please enter the point name', help='Name of Point')
@click.option('--apikey')
@main.command()
def SessionsPerPoint(point, datefrom, dateto, format, apikey):
    url = base_url + "/SessionsPerPoint/" + point + "/" +datefrom + "/" + dateto
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
@click.option('--apikey')
def healthcheck(apikey):
    url='http://localhost:8765/evcharge/api/admin/healthcheck'
    response = requests.get(url=url)
    print(response.json()) 

@main.command()
@click.option('--apikey')
def resetsessions(apikey):
    url='http://localhost:8765/evcharge/api/admin/resetsessions'
    response = requests.post(url=url)
    print(response.json())

@main.command()
@click.option('--station')
@click.option('--datefrom')
@click.option('--dateto')
@click.option('--format')
@click.option('--apikey')
def sessionsperstation(station, datefrom, dateto, format, apikey):
    url='http://localhost:8765/evcharge/api/SessionsPerStation/'+station+'/'+datefrom+'/'+dateto
    #url='http://localhost:8000/'+station+'/'+datefrom+'/'+dateto
    #print(url)
    filename = home + "/softeng20bAPI.token"
    newfile = home + "/SessionsPerStation_" + station + "_" + dateresolver(datefrom).replace('/','_') +  "_" + dateresolver(dateto).replace('/', '_') + '.' + format
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
@click.option('--ev')
@click.option('--datefrom')
@click.option('--dateto')
@click.option('--format')
@click.option('--apikey')
def sessionsperev(ev, datefrom, dateto, format, apikey):
    url='http://localhost:8765/evcharge/api/SessionsPerEV/'+ev+'/'+datefrom+'/'+dateto
    #url='http://localhost:8000/'+station+'/'+datefrom+'/'+dateto
    #print(url)
    filename = home + "/softeng20bAPI.token"
    newfile = home + "/SessionsPerEV_" + ev + "_" + dateresolver(datefrom).replace('/','_') +  "_" + dateresolver(dateto).replace('/', '_') + '.' + format
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
@click.option('--provider')
@click.option('--datefrom')
@click.option('--dateto')
@click.option('--format')
@click.option('--apikey')
def SessionsPerProvider(provider, datefrom, dateto, format, apikey):
    url='http://localhost:8765/evcharge/api/SessionsPerProvider/'+provider+'/'+datefrom+'/'+dateto
    filename = home + "/softeng20bAPI.token"
    newfile = home + "/SessionsPerProvider_" + provider + "_" + dateresolver(datefrom).replace('/','_') +  "_" + dateresolver(dateto).replace('/', '_') + '.' + format
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
@click.option('--usermod', is_flag=True)
@click.option('--username')
@click.option('--passw')
@click.option('--users')
@click.option('--sessionsupd', default=None)
@click.option('--source')
@click.option('--healthcheck', is_flag=True)
@click.option('--resetsessions', is_flag=True)
@click.option('--format')
@click.option('--apikey')
def admin(usermod, username, passw, users, sessionsupd, source, healthcheck, resetsessions, format, apikey):
    url = base_url + "/admin/"
    filename = home + "/softeng20bAPI.token"
    token = tokenizer(filename)
    if token != None:
        if usermod:
            url = url + 'usermod/'+username+'/'+passw
            r = requests.post(url, headers = {'X-OBSERVATORY-AUTH': 'Bearer '+apikey})
            if errorhandling(r):
                click.echo("The new user has been added successfully")


        elif healthcheck:
            url='http://localhost:8765/evcharge/api/admin/healthcheck'
            response = requests.get(url=url)
            print(response.json()) 

        elif resetsessions:
            url='http://localhost:8765/evcharge/api/admin/resetsessions'
            response = requests.post(url=url)
            print(response.json())


        elif users:
            url='http://localhost:8765/evcharge/api/admin/users/'+users
            filename = home + "/softeng20bAPI.token"
            newfile = home + "/User" + '.' + format
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



if __name__ == '__main__':
    main()



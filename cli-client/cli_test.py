import pytest
import os
import io
from ev_group05 import tokenizer

def test_login():

    a = os.popen('python3 ev_group05.py login --username user1 --passw userpass','r').read()
    assert a!= False

def test_badlogin():
    a = os.popen('python3 ev_group05.py login --username user3 --passw us312erpass','r').read()
    assert len(a) <= 100

def test_HealthCheck():
    a = os.popen('python3 ev_group05.py healthcheck','r')
    data = a.read()
    assert  'Healtchek data downloaded at /home/gestam/Healthcheck.json' in data

def test_Logout():
    os.system('python3 ev_group05.py login --username user1 --passw userpass')
    a = os.popen('python3 ev_group05.py logout','r').read()
    assert 'You have logged out. Goodbye!' in a

def test_SessionsPerPoint():
    os.system('python3 ev_group05.py login --username user1 --passw userpass')
    a = os.popen('python3 ev_group05.py sessionsperpoint --point 3 --datefrom 20190909 --dateto 20191010 --format json','r').read()
    assert 'Data downloaded' in a

def test_SessionsPerStation():
    os.system('python3 ev_group05.py login --username user1 --passw userpass')
    a = os.popen('python3 ev_group05.py sessionsperstation --station 13 --datefrom 20190909 --dateto 20191010 --format json','r').read()
    assert 'Data downloaded' in a

def test_SessionsPerEV():
    os.system('python3 ev_group05.py login --username user1 --passw userpass')
    a = os.popen('python3 ev_group05.py sessionsperev --ev 23 --datefrom 20190909 --dateto 20191010 --format json','r').read()
    assert 'Data downloaded' in a

def test_AdminUsers():
    os.system('python3 ev_group05.py login --username admin --passw 321nimda')
    a = os.popen('python3 ev_group05.py admin --users user1 --format json','r').read()
    assert '"id"' in a


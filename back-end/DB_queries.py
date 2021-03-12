import os
import hashlib
import datetime

from flask_mysqldb import MySQL
import mysql.connector


#@@@@@@@@@@@@@@@@@@@@@@-- DB conection --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   we are using the default port 3306

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sqlpassword'
app.config['MYSQL_DB'] = 'project_e_lectra'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #optional


mysql = MySQL(app)




#@@@@@@@@@@@@@@@@@@@@@@-- DB write/read --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def db_write(query, params):
    cur = mysql.connection.cursor()
    try:
        cur.execute(query, params)
        mysql.connection.commit()
        cur.close()

        return True

    except:
        cur.close()
        return False

def db_read(query, params=None):
    cur = mysql.connection.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)

    entries = cur.fetchall()
    cur.close()

    content = []

    for entry in entries:
        content.append(entry)

    return content

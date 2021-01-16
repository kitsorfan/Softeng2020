# e-Lectra Project by The Charging Aces:
# ~Stelios Kandylakis
# ~ Margarita  Oikonomakou
# ~Kitsos     Orfanopoulos
# ~Vasilis    Papalexis
# ~Georgia    Stamou
# ~Dido       Stoikou
# Softeng, ECE NTUA, 2021

#@@@@@@@@@@@@@@@@@@@@@---- CSV GENERATOR -----@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#We use 2 functions, random.randrange for numbers
#and random.choice for strings (see RANDOM DATA POOL)

NumberOfPoints=200 #Number of elements to produce

import random
import csv
import time
import decimal


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@-- Auxilary Function to create random date ----@@@@@@@@@@@@@@@@@@@


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#------------------------RANDOM DATA POOL-----------------------------------------
#Here we declare our random data pools. We make some lists with strings we will
#use below.The strings may be combined to create more random strings
#You can add as many strings as you want. The more the better.

#----Status ID------
StatusID=[1,1,1,1,1,1,1,2,3,4,5,6,7]

#----Point Type------
PointType=["AC2", "AC3","DC"]

#@@@@@@@@@@@@@@@@@@@@@@--- MAIN CODE ----@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with open('ChargingPoint.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #-- first row must have the names of the columns (attibutes of the entity)
    writer.writerow(["PointID", "StationID","PointType", "LastUpdate", "StatusID"])

    x=0
    while x<=NumberOfPoints:
        (


        writer.writerow([   #one single row contain:

            random.choice(PointType), #PointType
            LastUpdate=random_date("2020/1/1","2021/1/1",random.random()) #random date for last update
            random.choice(StatusID), #StatusID

        ])
        )
        x+=1


    print(".csv file produced correctly") #useless

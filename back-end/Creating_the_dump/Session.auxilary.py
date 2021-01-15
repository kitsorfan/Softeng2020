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

NumberOfSessions=1000 #Number of elements to produce
NumberOfProviders=6
NumberOfVehicles=35
NumberOfUsers=25
NumberOfPoints=200

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

#----Protocol------
Protocol=["OCCP","OCPI","OpenADR","ISO15118","OCHP","OICP"]
PricePolicies=["Standard","Standard","Standard","Standard","Standard","Discount","Discount","Discount","Fast Pro","Fast Pro","Fast Pro","Fast Pro","Military"]


#@@@@@@@@@@@@@@@@@@@@@@--- MAIN CODE ----@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with open('Session.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #-- first row must have the names of the columns (attibutes of the entity)
    #-- StationID isn't required (AUTO_INCREMENT)
    writer.writerow(["StartedOn", "FinishedOn","RequestedEnergy", "EnergyDelivered", "Protocol","PaymentType", "PricePolicyRef", "CostPerKWh","SessionCost", "BonusPointsRedeemed","BonusPointsGained","VehicleID","StationPointID","ProviderID"])

    x=0
    while x<=NumberOfSessions:
        StartDate=random_date("2020/1/1","2021/1/1",random.random())
        StartHour=random.randrange(0,20,1)
        EndHour=StartHour+random.randrange(1,3,1)
        StartMinutes=random.randrange(0,59,1)
        EndMinutes=random.randrange(0,59,1)
        StartSeconds=random.randrange(0,59,1)
        EndSeconds=random.randrange(0,59,1)

        StartedOn=StartDate+" "+str(StartHour)+":"+str(StartMinutes)+":"+str(StartSeconds)
        FinishedOn=StartDate+" "+str(EndHour)+":"+str(EndMinutes)+":"+str(EndSeconds)

        Energy=(random.randrange(150,375,1))/10
        EnergyOption=[str(Energy),"NULL"]

        RequestedEnergy=random.choice(EnergyOption)
        EnergyDelivered=round(Energy+(random.randrange(-10,10,1)/10),1)

        PricePolicyRef=random.choice(PricePolicies)
        if PricePolicyRef=="Standard":
            CostPerKWh=0.10
        elif PricePolicyRef=="Discount":
            CostPerKWh=0.08
        elif PricePolicyRef=="Fast Pro":
            CostPerKWh=0.16
        else: CostPerKWh=0.04

        BonusPointsGained=int(EnergyDelivered)
        BonusPointsRedeemed=random.randrange(0,2,1)*random.randrange(0,2,1)*random.randrange(0,200,1)


        SessionCost=round(CostPerKWh*EnergyDelivered-BonusPointsRedeemed/100,2)



        (
        writer.writerow([   #one single row contain:
        StartedOn, FinishedOn, RequestedEnergy, EnergyDelivered,
        random.choice(Protocol),
        "Credit Card",
        PricePolicyRef,CostPerKWh,SessionCost,BonusPointsRedeemed,BonusPointsGained,
        random.randrange(1,NumberOfVehicles,1),
        random.randrange(1,NumberOfPoints,1),
        random.randrange(1,NumberOfProviders,1)

        ])
        )
        x+=1


    print(".csv file produced correctly") #useless

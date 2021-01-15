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

NumberOfElements=1000 #Number of elements to produce

import random
import csv

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#------------------------RANDOM DATA POOL-----------------------------------------
#Here we declare our random data pools. We make some lists with strings we will
#use below.The strings may be combined to create more random strings
#You can add as many strings as you want. The more the better.

#----Station Name------
StationNamePrefix=['Electric', 'E-Autonomous','Super','BP', 'My','Public', 'Military', 'National','Euro']
StationNameSuffix=['Car','Station','Vehicle Charger','Home', "Car Plugin"]

#----Operator Name------
OperatorName=["Kostas", "Vasilis","Giorgos","Makis","Giannis","Manolis","Mixalis","Elena", "Maria","Marios","Dimitra","Stella","Xenia"]
OperatorSurname=["Papadopoulos","Papadakis","Georgiou","Oikonomou","Loulakis","Anastasiou","Takoroni","Sotiropoulos","Kapodistrias","Kolokotronis"]

#----Station Type------
StationType=["private","commercial","public","military"]

#----Street Name------
StreetName=["Kifisias", "Syggrou","Vasileos Konstantinou","Ilioupoleos","Oulof Palme","Katexaki","Kokkinopoulou","Peiraios","Iroon Politexneiou","Bouboulinas","Sotiros", "Agiou Alexandrou","Axilleos","Taxiarxon","Thiseos","Dionisiou Aeropagitou", "Ermou","Poseidonos"]

#----Town Name------
TownName=["Athens", "Thessaloniki", "Livadia", "Patra","Lamia","Alexandroupoli","Larisa","Karditsa","Trikala","Irakleio","Drama"]

#----Email------
EmailNamePrefix=["giorgos","user","giannis","maria","lord","favicon","provider","operator","john"]
EmailNameSuffix=["maestros","papadakis","supertroll","world","random","love","ellada","forthewin"]
EmailDomain=["info","gmail","yahoo","mailfence","protonmail","outlook","hotmail","mail.ntua","ece.ntua"]
Region=["gr","com","in","gov","met","uk","ger","us","eu","it"]

#----Website------
Website1=["www","telnet","snr","www2","email"]
Website2=["google","bing","fancy","webpage","mama","starwars","jurassic","poetry","legal","minister","filesystem"]
Website3=["ece.ntua","home","ntua","mechan","softeng"]
Webfile=["pdf","html","htm","mp4","mp3","json","docx","xlm","ddl"]


#@@@@@@@@@@@@@@@@@@@@@@--- MAIN CODE ----@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with open('Session.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #-- first row must have the names of the columns (attibutes of the entity)
    #-- StationID isn't required (AUTO_INCREMENT)
    writer.writerow(["StartedOn", "FinishedOn","RequestedAmountOfTime","RequestedEnergy", "EnergyDeliverd", "Protocol","PaymentType", "PricePolicyRef", "CostPerKWh","CostPerKWh","SessionCost", "BonusPointsRedeemed","BonusPointsGained","VehicleID","StationID","ProviderID"])

    x=0
    while x<=NumberOfElements:
        (
        writer.writerow([   #one single row contain:

        random.choice(StationNamePrefix)+" "+random.choice(StationNameSuffix),  #Station Name
        random.choice(OperatorName)+" "+random.choice(OperatorSurname), #Operator Name
        random.choice(StationType), #StationType
        random.choice(StreetName),   #Street Name
        random.randrange(1,256,1), #Street Number
        random.randrange(11111,99999,1),   #Postal Code (here 5 digits as string)
        random.choice(TownName), #Town
        "Greece",  #Country, we only use Greece for now
        random.randrange(37292524,39617083,10)/1000000, #Latitude (from -90 to 90, up to 8 decimals)
        random.randrange(21150551,24016207,10)/1000000, #Longitude (from -180 to 180, up to 9 decimals)
        random.randrange(1111111111,9999999999,1),    #Phone (int)
        random.choice(EmailNamePrefix)+random.choice(EmailNameSuffix)+str(random.randrange(1940,2021,1))+"@"+random.choice(EmailDomain)+"."+random.choice(Region),    #Email (format like '%_@_%._%')
        "https://"+random.choice(Website1)+"."+random.choice(Website2)+"."+random.choice(Website3)+"."+random.choice(Region)+"."+random.choice(Webfile), #Website (like  'https://_%._%', only https is allowed!)
        (random.randrange(0,250,1)+random.randrange(0,250,1))/100, #Rating Stars (decimal 4.2 default 0)
        random.randrange(0,200,1) #Total Votes (people who have voted)
        ])
        )
        x+=1


    print(".csv file produced correctly") #useless

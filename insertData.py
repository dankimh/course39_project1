import sqlite3
import os

db=sqlite3.connect('data/university.db')
cursor=db.cursor()

path="./data"
fileList=os.listdir(path)
csvList=[file for file in fileList if file.endswith(".csv")]

for file in csvList: #for each csv files
    
    tupleData=[]

    fo=open('data/'+file,'r')
    file=file[:-4] #delete filename extension(.csv)

    #print(file)
    csvFile=fo.read() #all data
    csvLine=csvFile.split('\n') #data split
    csvLine.pop(-1) #delete space
    #print(csvLine)
    
    for factor in csvLine: #for each line in file
        imsi=[]
        tempData=factor.split(',')
        #print(tempData)
        for cnt in tempData:
            imsi.append('?')
        #print(tempData)
        tupleData.append(tempData)
    tupleData.pop(0)
    tuple(tupleData)
    #print(tupleData)
    imsi=','.join(imsi)
    
    cursor.executemany('INSERT INTO '+file+'('+csvLine[0]+') VALUES('+imsi+')',tupleData)
#cursor.execute('''INSERT INTO classroom(building,room_number,capacity) VALUES(?,?,?)''',(a,b,c))
db.commit()

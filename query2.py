import sqlite3
import pandas as pd

db=sqlite3.connect('data/university.db')
cursor=db.cursor()

semesData=[]
max_count={}
max_name={}
count_name='''SELECT year,semester,name,count(*) from teaches natural join instructor GROUP BY year,semester,name'''

for row in cursor.execute(count_name):
    #print(row)
    semesData.append(row)
semesData.sort()

i=0
for tuple_1 in semesData:
    semester=str(semesData[i][0])+' '+semesData[i][1]
    try:
        if(max_count[semester]<semesData[i][3]):
            max_count[semester]=semesData[i][3]
            max_name[semester]=semesData[i][2]
        elif(max_count[semester]==semesData[i][3]):
            max_name[semester]+=(', '+semesData[i][2])
    except KeyError:
        max_count[semester]=semesData[i][3]
        max_name[semester]=semesData[i][2]
    i=i+1
    
columnList=['Semester','Name']
max_name=pd.DataFrame(max_name.items(),columns=columnList)
print(max_name)
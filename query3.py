import sqlite3
import pandas as pd

db=sqlite3.connect("data/university.db")
cursor=db.cursor()

time_slot_forenoon=''' SELECT distinct time_slot_id FROM time_slot WHERE start_hr>=8 and end_hr<12'''
section_forenoon=''' SELECT * FROM section natural join ('''+time_slot_forenoon+')'
forenoon_summer2010=''' SELECT * from ('''+section_forenoon+''') WHERE semester='Sumer' and year='2010' '''
room_capacity=''' SELECT distinct title,capacity FROM (classroom natural join ('''+forenoon_summer2010+')) natural join course'

max_capacity_course=[(0,0),]
titles=[]
for row in cursor.execute(room_capacity):
    print(row)
    if(max_capacity_course[0][1]<row[1]):
        del max_capacity_course[:]
        del titles[:]
        max_capacity_course.append(row)
        titles.append(row[0])
    elif(max_capacity_course[0][1]==row[1]):
        max_capacity_course.append(row)
        titles.append(row[0])

#print(titles)
columnList=['Title']
titles=pd.DataFrame(titles,columns=columnList)
print(titles)
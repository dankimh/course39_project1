import sqlite3
import pandas as pd

db=sqlite3.connect("data/university.db")
cursor=db.cursor()

#cursor.execute('''INSERT INTO instructor(ID,name,dept_name,salary) VALUES(12345,'imsi',?,1000)''',(None,))
db.commit()
rowData=[]
#print(type(cursor.execute('''SELECT * from `advisor` where i_ID=22222''')))
for row in cursor.execute('''SELECT coalesce(dept_name,'Unknown dept'),avg(salary) as avg_salary from `instructor` group by dept_name'''):
    #print(row)
    rowData.append(row)
columnList=['department','salary']
rowData=pd.DataFrame(rowData,columns=columnList)
print(rowData)
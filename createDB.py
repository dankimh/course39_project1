import sqlite3
from sqlite3 import OperationalError
db=sqlite3.connect('data/university.db')
cursor=db.cursor()

fo=open('DDL.sql','r')
sqlFile=fo.read()
fo.close()

sqlCommands=sqlFile.split(';')

for command in sqlCommands:
    cursor.execute(command)
db.commit()
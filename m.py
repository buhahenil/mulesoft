from msilib.schema import Error
import sqlite3
conn = sqlite3.connect('movies')

cur=conn.cursor
def sqlconn():
    try:
        con = sqlite3.connect('movies')
        print("Connection is created")
    except Error:
        print(Error)

#create database movies
tableQuery = ''' CREATE TABLE MOVIE(
                NAME TEXT,
                ACTOR TEXT,
                ACTRESS TEXT,
                DIRECTOR TEXT,
                YEAROFRELEASE TEXT)'''

#conn.execute(tableQuery)

#insart record
insertRecord = '''INSERT INTO MOVIE(NAME , ACTOR , ACTRESS , DIRECTOR , YEAROFRELEASE)
VALUES ('Singham','Ajay Devgn','Kareena Kapoor','	Rohit Shetty', 2011 )'''

conn.execute(insertRecord)

#show record
conn.execute('select * from movies')
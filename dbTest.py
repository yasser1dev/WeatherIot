import sqlite3
dbName="IotDatabase"
conn=sqlite3.connect(dbName)
curs=conn.cursor()

#statement='''INSERT INTO Tmp_Data (sensorId,date_time,temperature,temperature_level) VALUES(?,?,?,?) '''
#curs.execute(statement,('1s1s1','11-11-11',15,'ht'))
#conn.commit()
for rslt in curs.execute('''select * from Tmp_Data'''):
    print(rslt)

conn.close()

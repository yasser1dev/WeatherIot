import sqlite3

dbName="IotDatabase"
TableSchema=""" 
drop table if exists Tmp_Data;
create  Table Tmp_Data(
id integer primary key autoincrement,
sensorId text,
date_time text,
temperature decimal(6,2),
temperature_level text

);

drop table if exists Humidity_data;
create table Humidity_data(
id integer primary key autoincrement,
sensorId text,
date_time text,
humidity decimal(6,2),
humidity_level text
);

drop table if exists Acceleration_data;
create table Acceleration_data(
id integer primary key autoincrement,
sensorId text,
date_time text,
accX decimal(6,2),
accY decimal(6,2),
accZ decimal(6,2)
);
"""
#Connection
conn=sqlite3.connect(dbName)
curs=conn.cursor()

#Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

curs.close()
conn.close()
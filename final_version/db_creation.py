import sqlite3

DB_Name = "IoT_DataBase.db"
TableSchema=""" 
drop table if exists Temperature_Data;
create  Table Temperature_Data(
    id integer primary key autoincrement,
    sensor_id text,
    date_time text,
    temperature decimal(6,2),
    temperature_level text
);
drop table if exists Humidity_Data;
create table Humidity_Data(
    id integer primary key autoincrement,
    sensor_id text,
    date_time text,
    humidity decimal(6,2),
    humidity_level text
);
drop table if exists Acceleration_Data;
create table Acceleration_Data(
    id integer primary key autoincrement,
    sensor_id text,
    date_time text,
    accX decimal(6,2),
    accY decimal(6,2),
    accZ decimal(6,2)
);
"""
#Connect or create DB File
conn=sqlite3.connect(DB_Name)
curs=conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()

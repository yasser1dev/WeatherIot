import json
import sqlite3

DB_Name="IoT_DataBase.db"


class DataBaseManager():
    def __init__(self):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self,sql_query,args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return

    def select_db_record(self,sql_query,args=()):
        self.cur.execute(sql_query,args)
        self.conn.commit()
        return

    def select_db_record(self,sql_query,args=()):
        self.cur.execute(sql_query,args)
        self.conn.commit()
        return self.cur.fetchall();

    def __def__(self):
        self.cur.close()
        self.conn.close()
    @staticmethod
    def getDataSet(sqlText):
        dbObj=DataBaseManager()
        rows=dbObj.select_db_record(sqlText)
        del dbObj
        return rows

def Temperature_Data_Handler(jsonData):
    json_Dict=json.loads(jsonData)
    SensorID = json_Dict['sensor_id']
    Date_Time = json_Dict['date_time']
    Temperature = float(json_Dict['temperature'])
    TemperatureLevel = json_Dict['temperature_level']

    dbObj = DataBaseManager()
    dbObj.add_del_update_db_record("insert into Temperature_Data(sensor_id,date_time,temperature,temperature_level) values (?,?,?,?)",[SensorID,Date_Time,Temperature,TemperatureLevel])
    del dbObj
    print("Inserted Temperature Data into Database")
    print("")

def Humidity_Data_Handler(jsonData):
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['sensor_id']
    Date_Time = json_Dict['date_time']
    Humidity = float(json_Dict['humidity'])
    HumidityLevel = json_Dict['humidity_level']

    dbObj = DataBaseManager()
    dbObj.add_del_update_db_record("insert into Humidity_Data(sensor_id,date_time,humidity,humidity_level) values (?,?,?,?)",[SensorID,Date_Time,Humidity,HumidityLevel])
    del dbObj
    print("Inserted Humidity Data into Database.")
    print("")

def Acceleration_Data_Handler(jsonData):
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['sensor_id']
    Date_Time = json_Dict['date_time']
    print('******************',Date_Time)
    accX = float(json_Dict['accX'])
    accY = float(json_Dict['accY'])
    accZ = float(json_Dict['accZ'])

    dbObj = DataBaseManager()
    dbObj.add_del_update_db_record("insert into Acceleration_Data(sensor_id,date_time,accX,accY,accZ) values (?,?,?,?,?)",[SensorID,Date_Time,accX,accY,accZ])
    del  dbObj
    print("Inserted Acceleration Data into Database")
    print("")



def sensor_Data_Handler(Topic,jsonData):
    if Topic == "Home/BedRoom/DHT1/Temperature":
        Temperature_Data_Handler(jsonData)
    elif Topic == "Home/BedRoom/DHT1/Humidity":
        Humidity_Data_Handler(jsonData)
    elif Topic == "Home/BedRoom/DHT1/Acceleration":
        Acceleration_Data_Handler(jsonData)
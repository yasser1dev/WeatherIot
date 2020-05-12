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


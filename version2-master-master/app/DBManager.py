# coding=utf-8

from sqlalchemy import Column, String, Integer,Date,Time,DateTime,Boolean,Text,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

pymysql.install_as_MySQLdb()


class DBManager:
    #def __init__(self, db, host, usr, pwd, db_name):
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:0C45313cea34@47.107.86.216:3306/timecontrol')

    def create_session(self):
        # 创建DBSession类型
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        return session
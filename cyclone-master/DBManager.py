#coding=utf-8

#一组import引用
from sqlalchemy import  Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

pymysql.install_as_MySQLdb()

#数据库管理者类
class DBManager:
    def __init__(self,db,host,usr,pwd,db_name):
        self.engine=create_engine('mysql+mysqlconnector://root:0C45313cea34@47.107.86.216:3306/timecontrol')#连接数据库

    def create_session(self):
        #创建DBSession类型
        DBSession=sessionmaker(bind=self.engine)
        session=DBSession()
        return  session

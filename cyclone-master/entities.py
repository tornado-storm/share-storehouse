# coding = utf-8
#数据库存储信息模块

import json

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类：
Base = declarative_base()


# 用户实体类 数据表user
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表的结构
    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, nullable=False)
    account = sqlalchemy.Column(sqlalchemy.String(20), nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)

    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 任务实体类 数据表mission
class Mission(Base):
    # 表的名字
    __tablename__ = 'mission'

    # 表的结构
    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                                nullable=False)
    start_time = sqlalchemy.Column(sqlalchemy.Time, primary_key=True, nullable=False)
    date = sqlalchemy.Column(sqlalchemy.Date, primary_key=True, nullable=False)
    stop_time = sqlalchemy.Column(sqlalchemy.Time, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(20), nullable=False)
    label = sqlalchemy.Column(sqlalchemy.String(20), nullable=True)
    finish = sqlalchemy.Column(sqlalchemy.Boolean, default=0, nullable=False)
    alarm_time = sqlalchemy.Column(sqlalchemy.Time, nullable=True)
    repeat = sqlalchemy.Column(sqlalchemy.Boolean, default=0, nullable=True)


    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 给未来的信 Mail
class Mail(Base):
    __tablename__ = 'mail'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                                nullable=False)
    mail_time = sqlalchemy.Column(sqlalchemy.DateTime, primary_key=True, nullable=False)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 在日历中的对某一天的评价 comment
class Comment(Base):
    __tablename__ = 'comment'

    user_id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,
                                nullable=False)
    date = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    evaluate = sqlalchemy.Column(sqlalchemy.String(70), nullable=True)

    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json


# 每月生成的总结
class Summary(Base):
    __tablename__ = 'summary'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    date = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    sum = sqlalchemy.Column(sqlalchemy.Text, nullable=False)


    def to_json(self, message=None):
        dict = self.__dict__
        dict.pop("_sa_instance_state")
        if message is not None:
            print("additional")
            dict["msg"] = message.message
            dict["code"] = message.code
        print(dict)
        str_json = json.dumps(dict, ensure_ascii=False)
        return str_json

import json
from .DBManager import *
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类：
Base = declarative_base()
#from .exts import db

# 用户实体类 数据表user
class User(Base):
    # 表名
    __tablename__ = 'user'

    # 表的结构
    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    account = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)

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
    user_id = Column(Integer, primary_key=True,
                                nullable=False)
    start_time = Column(Time, primary_key=True, nullable=False)
    date = Column(Date, primary_key=True, nullable=False)
    stop_time = Column(Time, nullable=False)
    name = Column(String(20), nullable=False)
    label = Column(String(20), nullable=True)
    finish = Column(Boolean, default=0, nullable=False)
    alarm_time = Column(Time, nullable=True)
    repeat = Column(Boolean, default=0, nullable=True)


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

    user_id = Column(Integer, primary_key=True,
                                nullable=False)
    mail_time = Column(DateTime, primary_key=True, nullable=False)
    content = Column(Text, nullable=True)

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

    user_id = Column(Integer,primary_key=True,
                                nullable=False)
    date = Column(Date, nullable=False)
    evaluate = Column(String(70), nullable=True)

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

    user_id = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    sum = Column(Text, nullable=False)


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
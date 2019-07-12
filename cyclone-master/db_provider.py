# coding = utf-8

import pymysql


class DB(object):
    #类似于jAVA的构造函数，其中分别代表字符串，用户，密码，数据库
    def __init__(self, conn,usr,pwd,db_name):
        #类似JDBC:连接字符串，用户，密码，数据库
        self.db=pymysql.connect(conn,usr,pwd,db_name)

    def get_data(self,sql):
        #获取游标，cursor关键字表示光标，self表示对自身的引用
        cursor = self.db.cursor()
        #执行一个SQL语句
        cursor.execute(sql)
        #把游标抓取的数据取出来
        res=cursor.fetchall()
        return res

    def close(self):
        self.db.close()


# coding=utf-8
"""
SQLAlchemy: python中最有名的ORM框架
"""
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class MysqlDemo:
    def __init__(self):
        # 创建对象的基类:
        Base = declarative_base()

        # 定义User对象:
        class User(Base):
            # 表的名字:
            __tablename__ = 'user'

            # 表的结构:
            id = Column(String(20), primary_key=True)
            name = Column(String(20))

        # 初始化数据库连接:
        engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)

    def create(self):
        pass

    def retrieve(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class SqliteDemo:
    def __init__(self):
        # 创建对象的基类:
        Base = declarative_base()

        # 定义User对象:
        class User(Base):
            # 表的名字:
            __tablename__ = 'user'

            # 表的结构:
            id = Column(String(20), primary_key=True)
            name = Column(String(20))

        # 初始化数据库连接:
        engine = create_engine('sqlite:///./sqlalchemy.db')
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)

    def create(self):
        pass

    def retrieve(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    mysql = MysqlDemo()
    mysql.create()
    mysql.retrieve()
    mysql.update()
    mysql.delete()

    sqlite = SqliteDemo()
    sqlite.create()
    sqlite.retrieve()
    sqlite.update()
    sqlite.delete()

# coding:utf8
# 导入所需模块
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from contextlib import closing

# 生成sqlorm基类
Base = declarative_base()
# 创建数据库连接
engine = create_engine('sqlite:///./relation_demo.db')


# 目的是一个人可以拥有多本书，那么在数据库里的一对多关系
class User(Base):
    # 表名
    __tablename__ = 'user'
    # id字段
    id = Column(Integer, autoincrement=True, primary_key=True)
    # 名字字段
    name = Column(String(20), unique=True, nullable=False)
    # 一对多:
    # 内容不是表名而是定义的表结构名字
    books = relationship('Book')

    def __repr__(self):
        return f"User({self.id},{self.name}, {self.books})"


class Book(Base):
    # 表明
    __tablename__ = 'book'
    # id字段
    id = Column(Integer, autoincrement=True, primary_key=True)
    # 名字字段
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    # ForeignKey是外键 关联user表的id字段
    uname = Column(String(20), ForeignKey('user.name'))

    def __repr__(self):
        return f"Book({self.id},{self.name},{self.uname})"


# 创建所需表
if engine.dialect.has_table(engine, Book.__tablename__):
    Book.__table__.drop(engine)
if engine.dialect.has_table(engine, User.__tablename__):
    User.__table__.drop(engine)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    # 绑定,生成会话
    SessionCls = sessionmaker(bind=engine)
    with closing(SessionCls()) as session:
        # 创建用户
        liuyao = User(name='liuyao')
        ali = User(name='ali')
        # 添加字段
        session.add_all([liuyao, ali])
        # 提交
        session.commit()

    with closing(SessionCls()) as session:
        # 创建白鹿原这本书，指定谁是拥有者
        Whitedeer1 = Book(name='White_deer', uname='liuyao')
        # 创建三体这本书，指定谁是拥有者
        Threebody1 = Book(name='Three_body', uname='liuyao')
        Threebody2 = Book(name='Three_body', uname='ali')
        # 添加字段
        session.add_all([Whitedeer1, Threebody1, Threebody2])
        # 提交
        session.commit()

    with closing(SessionCls()) as s:
        print(s.query(User).filter(User.name == 'liuyao').one())
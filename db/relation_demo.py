# coding=utf8
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from contextlib import closing

Base = declarative_base()


class One2ManyDao:
    def __init__(self):
        # init db
        engine = create_engine('sqlite:///./relation_demo.db')
        if engine.dialect.has_table(engine, Book.__tablename__):
            Book.__table__.drop(engine)
        if engine.dialect.has_table(engine, User.__tablename__):
            User.__table__.drop(engine)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def add_users(self, usrs):
        with closing(self.Session()) as session:
            session.add_all(usrs)
            session.commit()

    def add_books(self, bks):
        with closing(self.Session()) as session:
            session.add_all(bks)
            session.commit()

    def get_user(self, name):
        with closing(self.Session()) as s:
            u = s.query(User).filter(User.name == name).one()
            bks = [One2ManyDao.Book(id=b.id, name=b.name, uname=b.uname) for b in u.books]
            return One2ManyDao.User(id=u.id, name=u.name, books=bks)

    class User:
        def __init__(self, id=None, name=None, books=[]):
            self.id = id
            self.name = name
            self.books = books

        def __repr__(self):
            return f"User({self.id},{self.name}, {self.books})"

    class Book:
        def __init__(self, id=None, name=None, uname=None):
            self.id = id
            self.name = name
            self.uname = uname

        def __repr__(self):
            return f"Book({self.id},{self.name},{self.uname})"


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    books = relationship('Book')

    # def __repr__(self):
    #     return f"User({self.id},{self.name}, {self.books})"


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    uname = Column(String(20), ForeignKey('user.name'))

    # def __repr__(self):
    #     return f"Book({self.id},{self.name},{self.uname})"


if __name__ == '__main__':
    dao = One2ManyDao()
    # add user
    usrs = [
        User(name='liuyao'),
        User(name='ali'),
    ]
    dao.add_users(usrs)
    # add books
    bks = [
        Book(name='White_deer', uname='liuyao'),
        Book(name='Three_body', uname='liuyao'),
        Book(name='Three_body', uname='ali'),
    ]
    dao.add_books(bks)
    # get user
    print(dao.get_user('liuyao'))

# coding=utf8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from contextlib import closing

Base = declarative_base()


class One2ManyDao:
    def __init__(self):
        # init db
        engine = create_engine('sqlite:///./relation_demo.db', echo=is_debug)
        if engine.dialect.has_table(engine, BookPO.__tablename__):
            BookPO.__table__.drop(engine)
        if engine.dialect.has_table(engine, UserPO.__tablename__):
            UserPO.__table__.drop(engine)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def add_users(self, usrs):
        with closing(self.Session()) as session:
            session.add_all(
                [UserPO(name=u.name, books=[BookPO(name=b.name, uname=u.name) for b in u.books]) for u in usrs])
            session.commit()

    def add_books(self, bks):
        with closing(self.Session()) as session:
            session.add_all([BookPO(name=b.name, uname=b.uname) for b in bks])
            session.commit()

    def get_user(self, name):
        with closing(self.Session()) as s:
            u = s.query(UserPO).filter(UserPO.name == name).one()
            return UserVO(id=u.id, name=u.name, books=[BookVO(id=b.id, name=b.name) for b in u.books])


class UserVO:
    def __init__(self, id=None, name=None, books=[]):
        self.id = id
        self.name = name
        self.books = books

    def __repr__(self):
        return f"User({self.id},{self.name}, {self.books})"


class BookVO:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Book({self.id},{self.name})"


class UserPO(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    books = relationship('BookPO')


class BookPO(Base):
    __tablename__ = 'book'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    uname = Column(String(20), ForeignKey('user.name'))


if __name__ == '__main__':
    is_debug = (input('is debug(y/n)?') == 'y')
    dao = One2ManyDao()
    # add user
    wd = BookVO(name='White_deer')
    tb = BookVO(name='Three_body')
    usrs = [
        UserVO(name='liuyao', books=[wd, tb]),
        UserVO(name='ali', books=[tb]),
    ]
    dao.add_users(usrs)
    # get user
    print(dao.get_user('liuyao'))

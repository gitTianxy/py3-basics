# coding=utf8
"""
ONE-2-MANY ORM
---
* 实现机制: `ForeignKey` & `relationship`
- `ForeignKey`: 含义为，其所在的列的值域应当被限制在另一个表的指定列的取值范围之类。
- `relationship`: 定义由外部连接得到的对象; 比如下方示例中和一个person相关的books被连接到person的books字段

* 类型: monodirectional vs bidirectional
- monodirectional: 只定义了一个relationship, 关联的双方只有一方可调用对方
- bidirectional: 定义了两个relationship, 连接的双方彼此可调用
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from contextlib import closing

Base = declarative_base()


class One2ManyDao:
    def __init__(self):
        # init db
        engine = create_engine('sqlite:///./relation_o2m.db', echo=is_debug)
        if engine.dialect.has_table(engine, BookPO.__tablename__):
            BookPO.__table__.drop(engine)
        if engine.dialect.has_table(engine, PersonPO.__tablename__):
            PersonPO.__table__.drop(engine)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def add_Persons(self, ps):
        with closing(self.Session()) as session:
            session.add_all(
                [PersonPO(name=p.name, books=[BookPO(name=b.name, pname=p.name) for b in p.books]) for p in ps])
            session.commit()

    def add_books(self, bks):
        with closing(self.Session()) as session:
            session.add_all([BookPO(name=b.name, pname=b.pname) for b in bks])
            session.commit()

    def get_Person(self, name):
        with closing(self.Session()) as s:
            p = s.query(PersonPO).filter(PersonPO.name == name).one()
            return PersonVO(id=p.id, name=p.name, books=[BookVO(id=b.id, name=b.name) for b in p.books])


class PersonVO:
    def __init__(self, id=None, name=None, books=[]):
        self.id = id
        self.name = name
        self.books = books

    def __repr__(self):
        return f"Person({self.id},{self.name}, {self.books})"


class BookVO:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Book({self.id},{self.name})"


class BookPO(Base):
    __tablename__ = 'book'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    pname = Column(String(20), ForeignKey('person.name'))
    # bidirectional
    # person = relationship('PersonPO', order_by=PersonPO.id.desc(), back_populates="books")


class PersonPO(Base):
    __tablename__ = 'person'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    # monodirectional
    books = relationship('BookPO', order_by=BookPO.id)
    # bidirectional
    # books = relationship('BookPO', order_by=BookPO.id, back_populates="person")


if __name__ == '__main__':
    is_debug = (input('is debug(y/n)?') == 'y')
    dao = One2ManyDao()
    # add Person
    wd = BookVO(name='White_deer')
    tb = BookVO(name='Three_body')
    usrs = [
        PersonVO(name='liuyao', books=[wd, tb]),
        PersonVO(name='ali', books=[tb]),
    ]
    dao.add_Persons(usrs)
    # get Person
    print(dao.get_Person('liuyao'))

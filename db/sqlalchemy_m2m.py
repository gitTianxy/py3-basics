# coding=utf8
"""
MANY 2 MANY ORM
---
* an association table
Many to Many adds `an association table` between two classes,
which is indicated by the secondary argument to relationship().
* back_populates
For a bidirectional relationship, both sides of the relationship contain a collection.
Specify using relationship.back_populates, and for each relationship() specify the common association table
* backref(simplify the definition)
When using the backref parameter instead of relationship.back_populates,
the backref will automatically use the same secondary argument for the reverse relationship
"""
from sqlalchemy import create_engine, Table, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from contextlib import closing

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('l_id', Integer, ForeignKey('left.id')),
                          Column('r_id', Integer, ForeignKey('right.id'))
                          )


class Left(Base):
    __tablename__ = 'left'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    rights = relationship(
        "Right",
        secondary=association_table,
        # back_populates="lefts"
        backref="lefts")

    def __repr__(self):
        return f"Left({self.id},{self.name},rights:{[(r.id, r.name) for r in self.rights]})"


class Right(Base):
    __tablename__ = 'right'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

    # lefts = relationship(
    #     "Left",
    #     secondary=association_table,
    #     back_populates="rights")

    def __repr__(self):
        return f"Right({self.id},{self.name},lefts:{[(l.id, l.name) for l in self.lefts]})"


class M2MDao:
    def __init__(self):
        # init db
        is_debug = (input("is debug(y/n)?") == 'y')
        eg = create_engine('sqlite:///./relation_m2m.db', echo=is_debug)
        self.Session = sessionmaker(bind=eg)
        if eg.dialect.has_table(eg, Left.__tablename__):
            Left.__table__.drop(eg)
        if eg.dialect.has_table(eg, Right.__tablename__):
            Right.__table__.drop(eg)
        Base.metadata.create_all(eg)

    def add_lefts(self, lefts):
        """
        equals 2 the operations below:
        ---
        BEGIN (implicit)
        INSERT INTO "right" (id, name) VALUES (?, ?)
            ((0, 'r_0'), (1, 'r_1'), (2, 'r_2'), (3, 'r_3'), (4, 'r_4'), ...
        INSERT INTO "left" (id, name) VALUES (?, ?)
            ((0, 'l_0'), (1, 'l_1'), (2, 'l_2'), (3, 'l_3'), (4, 'l_4'))
        INSERT INTO association (l_id, r_id) VALUES (?, ?)
            ((0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (0, 3), (1, 3), (2, 3),  ...
        COMMIT
        """
        with closing(self.Session()) as s:
            s.add_all(lefts)
            s.commit()

    def get_left(self, name):
        with closing(self.Session()) as s:
            l = s.query(Left).filter(Left.name == name).first()
            print(l)

    def get_right(self, name):
        with closing(self.Session()) as s:
            r = s.query(Right).filter(Right.name == name).first()
            print(r)


if __name__ == '__main__':
    rights = [Right(id=i, name=f"r_{i}") for i in range(10)]
    lefts = [Left(id=i, name=f"l_{i}", rights=rights[i:]) for i in range(5)]
    dao = M2MDao()
    # add left
    dao.add_lefts(lefts)
    # add right
    # get left
    dao.get_left('l_3')
    # get right
    dao.get_right('r_5')

# coding=utf8
"""
ONE-2-ONE ORM
---
One To One is essentially a bidirectional relationship with a scalar attribute on both sides.
To achieve this, the `uselist` flag indicates the placement of a scalar attribute instead of
a collection on the “many” side of the relationship.
"""
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from contextlib import closing

Base = declarative_base()


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    child = relationship("Child", uselist=False, back_populates="parent")

    def __repr__(self):
        return f"Parent({self.id},{self.name},child:{(self.child.id, self.child.name)})"


class Child(Base):
    __tablename__ = 'child'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    pname = Column(Integer, ForeignKey('parent.name'))
    parent = relationship("Parent", back_populates="child")

    def __repr__(self):
        return f"Child({self.id},{self.name},parent:{(self.parent.id, self.parent.name)})"


if __name__ == '__main__':
    # init db
    is_debug = (input('is debug(y/n)?') == 'y')
    eg = create_engine('sqlite:///./relation_o2o.db', echo=is_debug)
    if eg.dialect.has_table(eg, Child.__tablename__):
        Child.__table__.drop(eg)
    if eg.dialect.has_table(eg, Parent.__tablename__):
        Parent.__table__.drop(eg)
    Base.metadata.create_all(eg)
    Session = sessionmaker(bind=eg)
    # add parent
    p = Parent(name='Zhang')
    with closing(Session()) as s:
        s.add(p)
        s.commit()
    # add child
    c = Child(name='Xiao Zhang', pname='Zhang')
    with closing(Session()) as s:
        s.add(c)
        s.commit()
    # get parent
    with closing(Session()) as s:
        pvo = s.query(Parent).filter(Parent.name == 'Zhang').first()
        print(pvo)
    # get child
    with closing(Session()) as s:
        cvo = s.query(Child).filter(Child.name == 'Xiao Zhang').first()
        print(cvo)

# coding=utf-8
"""
SQLAlchemy: python中最有名的ORM框架
"""
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import exists, update, func
from contextlib import closing

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    sex = Column(String(10), nullable=False)
    age = Column(Integer)
    password = Column(String(20), nullable=False, default='1234')

    def __repr__(self):
        return f"User({self.name},{self.sex},{self.age},{self.password})"


class Email(Base):
    __tablename__ = 'email'

    id = Column(Integer, autoincrement=True, primary_key=True)
    address = Column(String(20), unique=True, nullable=False)
    uname = Column(String(20), nullable=False)

    def __repr__(self):
        return f"Email({self.id},{self.address},{self.uname})"


class MysqlDemo:
    """
    TODO
    """

    def __init__(self):
        """
        init db connection settings
        url for diff db-drivers:
            mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
            mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
            mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
        """
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
    """
    basic 'CRUD' examples of sqlite
    """

    def __init__(self):
        """
        init db connection settings
        """
        # 初始化数据库连接:
        self.eg = create_engine('sqlite:///./sqlite_demo.db')
        self.drop_tbls()
        Base.metadata.create_all(self.eg)
        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=self.eg)

    def add_u(self, u):
        print("add", u)
        with closing(self.DBSession()) as s:
            if self.exists(u):
                # raise RuntimeWarning(f"user named {u.name} already exists.")
                print(f"!!!user named '{u.name}' already exists.")
                return
            s.add(u)
            s.commit()

    def add_ulist(self, ulist):
        print("add user list", ulist)
        with closing(self.DBSession()) as s:
            s.add_all(ulist)
            s.commit()

    def retrieve(self, name):
        print("get by name:", name)
        with closing(self.DBSession()) as s:
            try:
                return s.query(User).filter(User.name == name).one()
            except NoResultFound:
                return None
            except:
                raise

    def get_ulist(self, order=0, offset=0, limit=5):
        print(f"get user list. order=age.{'ascend' if order==0 else 'desc'} offset={offset}, limit={limit}")
        with closing(self.DBSession()) as s:
            if order == 0:
                return list(s.query(User).order_by(User.age).offset(offset).limit(limit))
            else:
                return list(s.query(User).order_by(User.age.desc()).offset(offset).limit(limit))

    def update(self, u):
        print("update", u)
        with closing(self.DBSession()) as s:
            # method A
            # s.query(User).filter(User.name == u.name).update({
            #     "sex": u.sex,
            #     "age": u.age,
            #     "password": u.password
            # })
            # method B
            # stmt = update(User).where(User.name == u.name).values(
            #     sex=u.sex, age=u.age, password=u.password
            # )
            # s.execute(stmt)
            # method C(orm styled)
            for o in s.query(User).filter(User.name == u.name):
                o.sex = u.sex
                o.age = u.age
                o.password = u.password
            s.commit()

    def delete(self, name):
        with closing(self.DBSession()) as s:
            s.query(User).filter(User.name == name).delete()
            s.commit()

    def exec(self, sql, param):
        print("execute", sql)
        with closing(self.DBSession()) as s:
            res = s.execute(sql, param)
            for r in res:
                print(r)

    def count(self, sex):
        print("count", sex)
        with closing(self.DBSession()) as s:
            return s.query(User).filter(User.sex == sex).count()

    def exists(self, u):
        cond = exists().where(User.name == u.name)
        with closing(self.DBSession()) as s:
            return s.query(cond).scalar()

    def drop_tbls(self):
        if self.eg.dialect.has_table(self.eg, User.__tablename__):
            User.__table__.drop(self.eg)
        if self.eg.dialect.has_table(self.eg, Email.__tablename__):
            Email.__table__.drop(self.eg)

    def add_emails(self, emails):
        print("add", emails)
        with closing(self.DBSession()) as s:
            s.add_all(emails)
            s.commit()

    def get_user_email(self, name):
        """
        INNER JOIN demo
        ---
        SELECT User.*,Email.* FROM User INNER JOIN Email ON User.name=Email.uname
        WHERE User.name='name'
        """
        print(f"get user({name}) with email")
        with closing(self.DBSession()) as s:
            return s.query(User, Email) \
                .join(Email, User.name == Email.uname) \
                .filter(User.name == name) \
                .first()

    def get_user_emails(self):
        """
        LEFT JOIN demo
        ---
        SELECT User.*,Email.* FROM User LEFT JOIN Email ON User.name=Email.uname
        """
        print("get user-email associations")
        with closing(self.DBSession()) as s:
            return s.query(User, Email) \
                .outerjoin(Email, User.name == Email.uname) \
                .all()

    def get_user_ecounts(self):
        """
        SUB-QUERY demo
        ---
        SELECT User.*, ec.count FROM users LEFT OUTER JOIN
            (SELECT Email.uname, count(*) FROM Email GROUP BY Email.uname) AS ec
        ON User.name=ec.uname
        """
        print(f"get email count for users")
        with closing(self.DBSession()) as s:
            ec_stmt = s.query(Email.uname, func.count('*').label('count')) \
                .group_by(Email.uname) \
                .subquery()
            return s.query(User, ec_stmt.c.count) \
                .outerjoin(ec_stmt, User.name == ec_stmt.c.uname) \
                .all()


if __name__ == '__main__':
    # mysql = MysqlDemo()
    # mysql.create()
    # mysql.retrieve()
    # mysql.update()
    # mysql.delete()

    print("---sqlite demo")
    sqlite = SqliteDemo()
    kevin = User(name='kevin', sex='male', age=18, password='1234')
    sqlite.add_u(kevin)
    print(sqlite.retrieve('kevin'))
    ulist = [
        User(name='zhang1', sex='male', age=18, password='1234'),
        User(name='zhang2', sex='female', age=19),
        User(name='zhang3', sex='female', password='1234'),
    ]
    sqlite.add_ulist(ulist)
    sqlite.delete('zhang2')
    kevin_new = User(name='kevin', sex='male', age=30, password='2018')
    sqlite.update(kevin_new)
    print(sqlite.get_ulist(order=1))
    print(sqlite.count('female'))
    sqlite.exec(sql='select * from user where name=:name', param={'name': 'kevin'})
    print(sqlite.get_ulist())
    # email
    print("---join demo")
    e1 = Email(address='host1@mail.com', uname='kevin')
    e2 = Email(address='host2@mail.com', uname='kevin')
    sqlite.add_emails([e1, e2])
    print(sqlite.get_user_email('kevin'))
    print(sqlite.get_user_emails())
    print(sqlite.get_user_ecounts())

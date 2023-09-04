from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base

CONN = f'mysql+pymysql://{"root"}:{""}@{"localhost"}:{"3306"}/{"login"}'
engine = create_engine(CONN, echo=False)

Base = declarative_base()


def connsession():
    session = sessionmaker(bind=engine)

    return session()


session_db = connsession()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(LargeBinary)


Base.metadata.create_all(engine)

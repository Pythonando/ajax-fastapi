from venv import create
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine("sqlite:///sqlite.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    email = Column(String(100))
    senha = Column(String(16))

class Tokens(Base):
    __tablename__ = "Tokens"
    id = Column(Integer, primary_key=True)
    id_pressoa = Column(Integer, ForeignKey('pessoa.id'))
    token = Column(String(50))
    data = Column(DateTime, default=datetime.datetime.utcnow())


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    
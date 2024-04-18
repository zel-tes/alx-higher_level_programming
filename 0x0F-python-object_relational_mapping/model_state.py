''' the main() shows the states in the database "hbtn_0e_0_usa"
in order of their id '''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
connect_str = 'mysql://@localhost:3306/hbtn_0e_6_usa'
engine = create_engine(connect_str)
Base.metadata.create_all(engine)

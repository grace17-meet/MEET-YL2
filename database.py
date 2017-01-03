from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#TABLE INFORMATION ARE PLACED HERE.
class THE_TABLE_NAME(Base):
	__tablename__ = 'THE_TABLE_NAME'
	id = Column(Integer, primary_key=True)
	firstcol = Column(String(60))
	secondcol = Column(String(60))
	thirdcol = Column(String(60))
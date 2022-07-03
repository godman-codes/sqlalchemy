from sqlalchemy import ForeignKey, create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')

#base class
Base = declarative_base()

#create and engine
engine = create_engine(connection_string)


"""
   class Parent:
      id:int pk
      name:str


   class Child:
      id:int pk
      name:str
      parent_id:int fk (parent)
"""

class Parent(Base):
   __tablename__ = 'parents'
   id=Column(Integer(), primary_key=True)
   name=Column(String(25), nullable=False)
   child = relationship('Child', back_populates='parent', uselist=False, cascade= "all, delete")

   def __repr__(self) -> str:
      return f"<Parent {self.id}>"

class Child(Base):
   __tablename__ = 'children'
   id=Column(Integer(), primary_key=True)
   name=Column(String(25), nullable=False)
   parent_id=Column(Integer(), ForeignKey('parents.id', ondelete="CASCADE"))
   parent = relationship('Parent', back_populates='child')

   def __repr__(self) -> str:
      return f"<Child {self.id}>"
   

Base.metadata.create_all(engine)

#create a connection class
session = sessionmaker()(bind=engine)
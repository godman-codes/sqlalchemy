from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, ForeignKey, create_engine, String, Integer
import os

#create a BASE DIR
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

#create a connection string
connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'data1.db')

#create a Base Class
Base = declarative_base()

#create an engine
engine = create_engine(connection_string, echo=True)



"""
class User:
   id:int pk
   username:str
   email:str

class Post:
   id:int pk
   title:str
   content:str
   user_id:int fk
"""


class User(Base):
   __tablename__ = 'users'
   id = Column(Integer(), primary_key=True)
   username = Column(String(40), nullable=False, unique=True)
   email = Column(String(50), nullable=False, unique=True)
   #cascade to delete all relationships 
   #back populate for bi-directional relationship
   posts = relationship('Post', back_populates='author', cascade='all, delete')

   def __repr__(self) -> str:
      return f"<User {self.username}>"

class Post(Base):
   __tablename__ = 'posts'
   id = Column(Integer(), primary_key=True)
   title = Column(String(50), nullable=True)
   content = Column(String(255), nullable=False)
   user_id = Column(Integer(), ForeignKey('users.id'))
   #back populate for bi-directional relationship
   author = relationship('User', back_populates='posts')

   def __repr__(self) -> str:
      return f"<Post {self.title}>"

Base.metadata.create_all(engine)

#create a session
session = sessionmaker()(bind=engine)




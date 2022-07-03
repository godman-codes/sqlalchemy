from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Table
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'data2.db')

Base = declarative_base()

engine = create_engine(connection_string)

"""
table association:
   product_id: int fk(products.id)
   customer_id: int fk(customers.id) 

class Customer:
   id : int pk
   name : str

class product:
   id : int pk
   name : str
   price : int
   
"""
#create an association table 
association_table = Table(
   'association',
   Base.metadata,
   Column('customer_id', ForeignKey('customers.id')),
   Column('product_id', ForeignKey('products.id'))
)

class Customer(Base):
   __tablename__ = 'customers'
   id = Column(Integer(), primary_key = True)
   name = Column(String(), nullable=False)
   products = relationship('Product', secondary=association_table, back_populates='customers')

   def __repr__(self) -> str:
      return f"<Customer {self.name}>"

   
class Product(Base):
   __tablename__ = 'products'
   id = Column(Integer(), primary_key = True)
   name = Column(String(), nullable=False)
   price = Column(Integer(), nullable=False)
   customers = relationship('Customer', secondary=association_table, back_populates='products')


   def __repr__(self) -> str:
      return f"<Product {self.name}>"   

Base.metadata.create_all(engine)

session = sessionmaker()(bind=engine)
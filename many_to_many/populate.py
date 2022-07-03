from main import session, Customer, Product

# customer1 = Customer(name="Customer 1")
# customer2 = Customer(name="Customer 2")
# customer3 = Customer(name="Customer 3")

customer1 = session.query(Customer).filter_by(id=1).first()
customer2 = session.query(Customer).filter_by(id=2).first()
customer3 = session.query(Customer).filter_by(id=3).first()



product1 = Product(name='Chicken', price=2000)
product2 = Product(name='Bread', price=1000)
product3 = Product(name='Milk', price=500)

#this automatically adds the product to the product table 
customer1.products.append(
   product2
)
customer1.products.append(
   product3
)

print(customer1.products)


# session.add_all([product1, product2, product3])
session.commit()


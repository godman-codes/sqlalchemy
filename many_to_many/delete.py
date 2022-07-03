from main import session, Product, Customer

customer = session.query(Customer).filter_by(id=1).first()

product=session.query(Product).filter_by(id=1).first()

#to remove product from its associate table
customer.products.remove(product)

session.commit()
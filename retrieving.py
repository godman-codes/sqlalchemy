from main import User, Session, engine

local_session = Session(bind=engine)

#returns all object in users table in form of lists
# users = local_session.query(User).all()[:3]
# for user in users:
#    print(user.username)

#query for one object
user = local_session.query(User).filter(User.username=="jona").first()

print(user)

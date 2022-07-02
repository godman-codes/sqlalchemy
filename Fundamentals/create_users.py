from main import User, Session, engine

#new users
users = [
   {
      "username": "jerry",
      "email": "jerry@company.com"
   },
   {
      "username": "jordan",
      "email": "jordan@company.com"
   },
   {
      "username": "jackson",
      "email": "jsckson@company.com"
   },
   {
      "username": "john",
      "email": "john@company.com"
   },
   {
      "username": "jack",
      "email": "jack@company.com"
   },
   {
      "username": "james",
      "email": "james@company.com"
   },
]


#binding session to engine
local_session = Session(bind=engine)

#create the new user
# new_user = User(username="jona", email="jona@company.com")

#add the new user to the local_session
# local_session.add(new_user)

#commit the new user using local session
# local_session.commit()

#loop through the populated users assign the data to the User class using the dictionary keys
for u in users:
   new_user = User(username=u['username'], email=u['email'])

   local_session.add(new_user)

   local_session.commit()

   print(f"added {u['username']}")
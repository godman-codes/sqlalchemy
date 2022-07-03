from main import engine, Parent, Child, session

# parent1 = Parent(name='Parent 1')
# parent2 = Parent(name='parent 2')

# session.add_all(
#    [parent1, parent2]
# )

# session.commit()

# parents = session.query(Parent).all()
# print(parents)

parent1 = session.query(Parent).filter_by(id=1).first()
print(parent1)

# child1 = Child(name="Child 1", parent=parent1)

# session.add(child1)
# session.commit()

child2 = Child(name="Child 2", parent=parent1)

session.add(child2)
session.commit()


print(parent1.child)
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group

fake = Faker()
engine = create_engine('sqlite:///database.db')  # Підставте свій URL бази даних
Session = sessionmaker(bind=engine)
session = Session()

# Додавання студентів
for _ in range(30):
    student = Student(fullname=fake.name(), group_id=fake.random_int(min=1, max=3))
    session.add(student)

session.commit()

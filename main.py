import argparse
from models import Teacher, Group, Student, Subject, Grade
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

parser = argparse.ArgumentParser(description='CRUD operations on the database')
parser.add_argument('--action', '-a', choices=['create', 'list', 'update', 'remove'], required=True)
parser.add_argument('--model', '-m', choices=['Teacher', 'Group', 'Student', 'Subject', 'Grade'], required=True)

args = parser.parse_args()

if args.action == 'create':
    if args.model == 'Teacher':
        name = input("Enter teacher's name: ")
        teacher = Teacher(name=name)
        session.add(teacher)
        session.commit()
    elif args.model == 'Group':
        name = input("Enter group's name: ")
        group = Group(name=name)
        session.add(group)
        session.commit()
elif args.action == 'list':
    if args.model == 'Teacher':
        teachers = session.query(Teacher).all()
        for teacher in teachers:
            print(f"Teacher ID: {teacher.id}, Name: {teacher.name}")
    elif args.model == 'Group':
        groups = session.query(Group).all()
        for group in groups:
            print(f"Group ID: {group.id}, Name: {group.name}")
elif args.action == 'update':
    if args.model == 'Teacher':
        teacher_id = int(input("Enter teacher's ID to update: "))
        teacher = session.query(Teacher).filter_by(id=teacher_id).first()
        if teacher:
            new_name = input("Enter the new name for the teacher: ")
            teacher.name = new_name
            session.commit()
        else:
            print("Teacher not found.")
elif args.action == 'remove':
    if args.model == 'Teacher':
        teacher_id = int(input("Enter teacher's ID to remove: "))
        teacher = session.query(Teacher).filter_by(id=teacher_id).first()
        if teacher:
            session.delete(teacher)
            session.commit()
        else:
            print("Teacher not found.")

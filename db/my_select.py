from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import Student, Grade
from sqlalchemy import desc

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    query = session.query(Student.fullname, func.round(func.avg(Grade.score), 2).label('avg_score'))
    query = query.join(Grade).group_by(Student.id).order_by(desc('avg_score')).limit(5)
    return query.all()

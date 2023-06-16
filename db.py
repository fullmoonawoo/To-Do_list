import sqlite3
from sqlalchemy import create_engine, Column, String, Date, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

#connection = sqlite3.connect("to-do_tasks.db")

#cursor = connection.cursor()

#cursor.execute("ANY SQLite3 Syntax")

#connection.commit()
#connection.close()

#  SQLAlchemy commands use without sqlite syntax

db_path = "tasks.db"
engine = create_engine(f'sqlite:///{db_path}', echo=True)
Base = declarative_base()


class Tasks(Base):
    __tablename__ = "Running tasks"
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(String)
    progress = Column(Integer)
    remained = Column(Integer)

    def __str__(self):
        return f'ID: {self.id}, TASK: {self.task}, DEADLINE: {self.deadline}, PROGRESS: {self.progress}, REMAINED: {self.remained}'


# Create the tables
#Base.metadata.create_all(engine) # if db is created need to be disable

Session = sessionmaker(bind=engine)
session = Session()


def add_new_task(task_info, deadline, progress, remained):
    task = Tasks(task=task_info, deadline=deadline, progress=progress, remained=remained)  # here will be output from backend
    session.add(task)
    session.commit()
    session.close()


def get_tasks():
    db_values = session.query(Tasks).all()
    return db_values


def remove_task():
    db_val = session.query(Tasks).all()
    print(db_val)
    for row in db_val:
        session.delete(row)
        session.commit()
        session.close()
    print(db_val)


result = get_tasks()

for x in result:
    print(x.task, x.deadline, x.progress, x.remained)

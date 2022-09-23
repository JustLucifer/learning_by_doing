from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Date
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pySimpleGUI/ToDoApp/tasks.sqlite3')
Base = declarative_base()


class Task(Base):
    __tablename__ = 'active_tasks'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    task = Column(String(100))
    priority = Column(Integer)


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    task = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

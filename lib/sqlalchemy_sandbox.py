#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    # Create an SQLite database in memory.
    engine = create_engine('sqlite:///students.db', echo=True)

    # Create the tables in the database (based on the Base metadata)
    Base.metadata.create_all(engine)

#!/usr/bin/python3
"""
 a script that deletes all State objects with a name
 containing the letter a from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(state[0] + ": (" + str(state[1]) + ") " + state[2])

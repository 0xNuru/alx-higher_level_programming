#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

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

    states = session.query(State).filter(State.name.like("%a%")).order_by(State.id)

    for state in states:
        print(state.id, state.name, sep=": ")

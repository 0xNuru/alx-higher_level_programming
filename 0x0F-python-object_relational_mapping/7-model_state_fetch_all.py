#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = "hbtn_0e_6_usa"

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print(state.id, state.name, sep=": ")

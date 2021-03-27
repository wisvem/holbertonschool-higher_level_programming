#!/usr/bin/python3
"""First usage of SLQAlchemy"""
from sys import argv
import json
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    myU = argv[1]
    myP = argv[2]
    myDB = argv[3]
    myH = "localhost"

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(myU, myP, myDB)
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    presession = sessionmaker(bind=engine)
    session = presession()
    result = session.query(State).order_by(State.id).all()

    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()

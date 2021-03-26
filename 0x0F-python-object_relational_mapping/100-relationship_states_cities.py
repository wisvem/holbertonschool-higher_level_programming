#!/usr/bin/python3
"""First usage of SLQAlchemy"""
from sys import argv
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

    myC = "San Francisco"
    myS = "California"

    record = State(name=myS)
    c = City(name=myC)
    record.cities.append(c)
    session.add(record)
    session.commit()
    session.close()

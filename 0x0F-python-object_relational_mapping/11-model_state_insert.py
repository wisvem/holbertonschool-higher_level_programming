#!/usr/bin/python3
"""First usage of SLQAlchemy"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

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
    sName = "Louisiana"
    record = State(name=sName)
    session.add(record)
    session.commit()
    result = session.query(State).filter_by(name=sName).first()
    print(result.id)
    session.close()

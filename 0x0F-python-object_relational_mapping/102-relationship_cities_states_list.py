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
    result = session.query(State.id.label('sid'),
                           State.name.label('sname'),
                           City.id.label('cid'),
                           City.name.label('cname'))\
        .filter(City.state_id == State.id)
    prev_sid = 0
    for r in result:
        print("{}: {} -> {}".format(r.cid, r.cname, r.sname))
    session.close()

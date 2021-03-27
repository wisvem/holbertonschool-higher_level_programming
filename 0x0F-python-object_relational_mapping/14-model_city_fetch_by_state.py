#!/usr/bin/python3
"""First usage of SLQAlchemy"""
from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    myU = argv[1]
    myP = argv[2]
    myDB = argv[3]
    myH = "localhost"
    city = "City"
    states = "states"
    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(myU, myP, myDB)
    engine = create_engine(db, pool_pre_ping=True)
#    State.cities = relationship(city, order_by=City.id, back_populates=states)

    Base.metadata.create_all(engine)

    presession = sessionmaker(bind=engine)
    session = presession()
    result = session.query(State.name, City.id, City.name.label('cname'))\
        .filter(City.state_id == State.id)
#    print(result)
    for c in result:
        print("{}: ({}) {}".format(c.name, c.id, c.cname))
    session.close()

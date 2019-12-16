#!/usr/bin/python3
"""
changes the name of a State object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Mysession = Session()

    stateUpdated = Mysession.query(State).filter(State.id == 2).first()

    if stateUpdated:
        stateUpdated.name = 'New Mexico'
        Mysession.commit()

#!/usr/bin/python3
"""Script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    state_query = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    # Delete all the instances of state with a name containing the letter a
    [session.delete(state) for state in state_query]
    session.commit()
    Base.metadata.create_all(engine)
    session.close()

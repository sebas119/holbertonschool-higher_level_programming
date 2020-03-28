#!/usr/bin/python3
"""Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    new_state = State(name='Louisiana')
    # Add the transaction to session
    session.add(new_state)
    # Flush pending changes and commit the current transaction
    session.commit()
    state = session.query(State).filter_by(name='Louisiana').one()
    print(state.id)
    Base.metadata.create_all(engine)
    session.close()

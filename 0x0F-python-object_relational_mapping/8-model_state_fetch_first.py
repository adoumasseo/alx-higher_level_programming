#!/usr/bin/python3
"""
    List all state objects from the database using SQLAlchemy
"""
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    first_state = session.query(State).first()
    if first_state is None:
        print("Nothing")
    print('{}: {}'.format(first_state.id, first_state.name))
    session.close()

#!/usr/bin/python3
"""
    This Module contain the model for class State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, MetaData

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
        Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

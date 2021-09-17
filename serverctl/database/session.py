"""
Contains the database configuration and functions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from serverctl.config import settings

sqlalchemy_database_url = settings.database_url

engine = create_engine(sqlalchemy_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

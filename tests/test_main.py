"""
Tests for miscellaneous routes defined in main.py
"""

from typing import Any, Generator

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from serverctl.config import settings
from serverctl.database.base import Base
from serverctl.main import app, get_db

sqlalchemy_database_url = settings.database_url

engine = create_engine(
    sqlalchemy_database_url, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def _override_get_db() -> Generator[Any, None, None]:
    try:
        database = TestingSessionLocal()
        yield database
    finally:
        database.close()


app.dependency_overrides[get_db] = _override_get_db

client = TestClient(app)


def test_root() -> None:
    """Test root route"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Working!"
    }

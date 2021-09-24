"""Conftest."""
import pytest
from app.data.entities import User
from app.data.repositories.user_repository import UserRepositoryMock


@pytest.fixture(scope="function")
def data():
    """Fixture."""
    users = [
        User(
            id=1,
            name="Test1",
            surname="Testov1"
        ),
        User(
            id=2,
            name="Test2",
            surname="Testov2"
        ),
        User(
            id=3,
            name="Test3",
            surname="Testov3"
        ),
    ]

    return users

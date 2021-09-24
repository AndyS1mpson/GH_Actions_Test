"""Test for working with user data."""
from app.data.entities import User
from app.data.repositories.user_repository import UserRepositoryMock


def test_get_user_by_id(data):
    """Test getting user by user id."""
    user_repository = UserRepositoryMock(data)

    user = user_repository.get_user_by_id(1)

    assert user.name == 'Test1'
    assert user.surname == 'Testov'


def test_create_user(data):
    """Test user creation."""
    user_repository = UserRepositoryMock(data)

    user = User(
        id=4,
        name="Test4",
        surname='Testov4'
    )

    user_repository.create_user(user)

    assert len(user_repository.users) == 4
    assert user_repository.users[-1].name == user.name
    assert user_repository.users[-1].surname == user.surname
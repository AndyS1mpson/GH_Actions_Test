"""UserRepositoryMock class."""
from typing import List
from app.data.entities import User


class UserRepositoryMock:
    """Class for manipulating user data."""

    users: List[User] = list()

    def __init__(self, users: List[User]) -> None:
        """Initialize class.

        Args:
            users (List[User]): list of mock users data.
        """
        self.users = users
    
    def get_user_by_id(self, id: int) -> User:
        """Get user by user id.

        Args:
            id (int): user id.

        Returns:
            User: user data.
        """
        user = [u for u in self.users if u.id == id]
        if len(user) == 0:
            return None
        return user[0]

    def create_user(self, user: User) -> None:
        """Create user.

        Args:
            user (User): new user.
        """
        self.users.append(user)

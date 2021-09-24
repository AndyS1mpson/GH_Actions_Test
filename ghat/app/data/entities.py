"""Entities."""
from dataclasses import dataclass

@dataclass
class User:
    """User entity."""

    id: int
    name: str
    surname: str

from typing import Dict, List, Optional
from datetime import datetime

class Book:
    def __init__(self, id: int, title: str, author: str, isbn: str, 
                 quantity: int = 1):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.available = quantity

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'quantity': self.quantity,
            'available': self.available
        }

class Member:
    def __init__(self, id: int, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.borrowed_books: List[int] = []  # Store book IDs

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'borrowed_books': self.borrowed_books
        }

# In-memory storage
books: Dict[int, Book] = {}
members: Dict[int, Member] = {}

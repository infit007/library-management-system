from flask import Blueprint, request, jsonify
from typing import Dict, List
from models import Book, books
from auth import verify_token

books_bp = Blueprint('books', __name__)

@books_bp.route('/', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    
    result = books.values()
    if title:
        result = filter(lambda b: title.lower() in b.title.lower(), result)
    if author:
        result = filter(lambda b: author.lower() in b.author.lower(), result)
    
    return jsonify([book.to_dict() for book in result])

@books_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id: int):
    book = books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.to_dict())

@books_bp.route('/', methods=['POST'])
def create_book():
    token = request.headers.get('Authorization')
    if not verify_token(token):
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    if not all(k in data for k in ['title', 'author', 'isbn']):
        return jsonify({'error': 'Missing required fields'}), 400

    book_id = len(books) + 1
    book = Book(
        id=book_id,
        title=data['title'],
        author=data['author'],
        isbn=data['isbn'],
        quantity=data.get('quantity', 1)
    )
    books[book_id] = book
    return jsonify(book.to_dict()), 201

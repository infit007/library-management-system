from flask import Blueprint, request, jsonify
from typing import Dict, List
from models import Member, members
from auth import verify_token, hash_password

members_bp = Blueprint('members', __name__)

@members_bp.route('/', methods=['GET'])
def get_members():
    return jsonify([member.to_dict() for member in members.values()])

@members_bp.route('/<int:member_id>', methods=['GET'])
def get_member(member_id: int):
    member = members.get(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    return jsonify(member.to_dict())

@members_bp.route('/', methods=['POST'])
def create_member():
    data = request.get_json()
    if not all(k in data for k in ['name', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400

    member_id = len(members) + 1
    member = Member(
        id=member_id,
        name=data['name'],
        email=data['email'],
        password=hash_password(data['password'])
    )
    members[member_id] = member
    return jsonify(member.to_dict()), 201

@members_bp.route('/<int:member_id>', methods=['PUT'])
def update_member(member_id: int):
    token = request.headers.get('Authorization')
    if not verify_token(token):
        return jsonify({'error': 'Unauthorized'}), 401

    member = members.get(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    data = request.get_json()
    if 'name' in data:
        member.name = data['name']
    if 'email' in data:
        member.email = data['email']
    if 'password' in data:
        member.password = hash_password(data['password'])

    return jsonify(member.to_dict())

@members_bp.route('/<int:member_id>/borrow/<int:book_id>', methods=['POST'])
def borrow_book(member_id: int, book_id: int):
    token = request.headers.get('Authorization')
    if not verify_token(token):
        return jsonify({'error': 'Unauthorized'}), 401

    member = members.get(member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    if book_id in member.borrowed_books:
        return jsonify({'error': 'Book already borrowed'}), 400

    member.borrowed_books.append(book_id)
    return jsonify(member.to_dict())

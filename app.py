from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# In-memory databases
books_db = {}
members_db = {}
tokens = {"admin_token": "admin"}  # Simple token system

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Library Management System!"}), 200

if __name__ == '__main__':
    app.run(debug=True)

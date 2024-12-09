from flask import Flask
from routes.books import books_bp
from routes.members import members_bp

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.register_blueprint(books_bp, url_prefix='/api/books')
    app.register_blueprint(members_bp, url_prefix='/api/members')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from .database import init_db

def create_app():
    app = Flask(__name__, template_folder="../templates")

    # Crear la base de dades si no existeix
    init_db()

    from .routes import main
    app.register_blueprint(main)

    return app
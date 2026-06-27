from flask import Flask
from .database import init_db
import logging

def create_app():
    app = Flask(__name__, template_folder="../templates")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Crear la base de dades si no existeix
    init_db()

    from .routes import main
    app.register_blueprint(main)

    return app
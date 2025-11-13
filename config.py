from dotenv import dotenv_values
import os

class Config:
    config = dotenv_values(".env")

    SECRET_KEY = config['SECRET_KEY']
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

    DATABASE_USERNAME = config['DATABASE_USERNAME']
    DATABASE_PASSWORD = config['DATABASE_PASSWORD']
    DATABASE_HOST = config['DATABASE_HOST']
    DATABASE_PORT = config['DATABASE_PORT']
    DATABASE_NAME = config['DATABASE_NAME']

    # Ruta al certificado SSL que descargaste desde Aiven
    SSL_CA = os.path.join(os.path.dirname(__file__), "certs/ca.pem")

    # Cadena de conexión completa para SQLAlchemy + MySQL + SSL
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}"
        f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        f"?ssl_ca={SSL_CA}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"

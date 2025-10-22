from dotenv import dotenv_values

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

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"
    
class TestingConfig(Config):
    """Testing configuration."""
    config = dotenv_values(".env")  # Cargar valores desde el archivo .env

    DATABASE_USERNAME = config['DATABASE_USERNAME']
    DATABASE_PASSWORD = config['DATABASE_PASSWORD']
    DATABASE_HOST = config['DATABASE_HOST']
    DATABASE_PORT = config['DATABASE_PORT']
    DATABASE_NAME = config['DATABASE_NAME']
    TESTING = True
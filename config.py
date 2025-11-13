from dotenv import dotenv_values
import os

class Config:

    IS_RAILWAY = os.getenv("RAILWAY_ENVIRONMENT") is not None

    if IS_RAILWAY:
        env = os.environ
    else:
        # Local 
        env = dotenv_values(".env")

    SECRET_KEY = env.get("SECRET_KEY")
    SERVER_NAME = "0.0.0.0:5000"
    DEBUG = not IS_RAILWAY  # Local da True

    DATABASE_USERNAME = env.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = env.get('DATABASE_PASSWORD')
    DATABASE_HOST = env.get('DATABASE_HOST')
    DATABASE_PORT = env.get('DATABASE_PORT')
    DATABASE_NAME = env.get('DATABASE_NAME')

    SSL_CA = env.get("AIVEN_CA")

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"

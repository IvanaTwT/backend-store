import mysql.connector

class DatabaseConnection:
    _config = None

    @classmethod
    def set_config(cls, config):
        cls._config = config

    @classmethod
    def get_new_connection(cls):
        return mysql.connector.connect(
            host=cls._config['DATABASE_HOST'],
            user=cls._config['DATABASE_USERNAME'],
            port=cls._config['DATABASE_PORT'],
            password=cls._config['DATABASE_PASSWORD'],
            database=cls._config['DATABASE_NAME'],
            ssl_ca=cls._config.get("SSL_CA")
        )

    @classmethod
    def execute_query(cls, query, params=None):
        conn = cls.get_new_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(query, params)
            conn.commit()
            return cursor
        except Exception as e:
            conn.rollback()
            print("DB ERROR:", e)
            raise
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def fetch_one(cls, query, params=None):
        conn = cls.get_new_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @classmethod
    def fetch_all(cls, query, params=None):
        conn = cls.get_new_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
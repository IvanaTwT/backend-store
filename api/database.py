import mysql.connector

class DatabaseConnection:
    _config = None

    @classmethod
    def set_config(cls, config):
        cls._config = config

    @classmethod
    def _new_connection(cls):
        """Crear una conexión nueva"""
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
        conn = cls._new_connection()     
        cursor = conn.cursor()
        cursor.execute("SET innodb_lock_wait_timeout = 5")
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    @classmethod
    def fetch_all(cls, query, params=None):
        conn = cls._new_connection()     
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    @classmethod
    def fetch_one(cls, query, params=None):
        conn = cls._new_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
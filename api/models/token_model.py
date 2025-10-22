from ..database import DatabaseConnection
from datetime import datetime, timedelta, UTC
from config import Config
import jwt

class Token:
    """Clase que representa la gestión de tokens."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.user_id = kwargs.get('user_id')
        self.token = kwargs.get('token')
        self.created_at = kwargs.get('created_at')
        self.expired_at = kwargs.get('expired_at')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "token": self.token,
            "created_at": self.created_at,
            "expired_at":self.expired_at
        }

    @classmethod
    def create_token(cls, user_id):
        """
        Crear y almacenar un token para un usuario.
        """
        Token.delete_expired_tokens()#eliminar tokens expirados
        if not user_id:
            return None
        payload = {
            "user_id": user_id,
            "exp": datetime.now(UTC) + timedelta(days=1)
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
        query = """
            INSERT INTO ecommerce.tokens (user_id, token, created_at, expired_at)
            VALUES (%(user_id)s, %(token)s, %(created_at)s, %(expired_at)s)
        """
        params = {
            "user_id": int(user_id),
            "token": token
            , "created_at": datetime.now()
            ,"expired_at":  payload["exp"]
        }
        DatabaseConnection.execute_query(query=query, params=params)
        return token

    @classmethod
    def get_token(cls, token):
        """
        Obtener un token desde la base de datos.
        """
        query = """
            SELECT id, user_id, token, created_at, expired_at
            FROM tokens
            WHERE token = %(token)s
            """
        result = DatabaseConnection.fetch_one(query, {"token": token})
        if result:
            return cls(id=result[0], user_id=result[1], token=result[2], created_at=result[3], expired_at=result[4])
        return  None

    @classmethod
    def delete_token(cls, token):
        """
        Eliminar un token de la base de datos.
        """
        query = "DELETE FROM tokens WHERE token = %(token)s"
        params = {"token": token}
        DatabaseConnection.execute_query(query, params)
        return {"message": "Token eliminado"}

    @classmethod
    def get_tokens_by_user(cls, user_id):
        """
        Obtener todos ultimo token del usuario.
        """
        query = """
            SELECT id, user_id, token, created_at, expired_at
            FROM tokens
            WHERE user_id = %(user_id)s
            limit 1;
        """
        if not user_id:
            return None
        result = DatabaseConnection.fetch_one(query, {"user_id": user_id})
        if result:
            return cls(id=result[0], user_id=result[1], token=result[2], created_at=result[3], expired_at=result[4])
        return None

    @classmethod
    def delete_all_tokens(cls, user_id):
        """
        Eliminar todos los tokens de un usuario.
        """
        query = "DELETE FROM tokens WHERE user_id = %(user_id)s"
        params = {"user_id": user_id}
        DatabaseConnection.execute_query(query, params)
        return {"message": f"Todos los tokens del usuario {user_id} eliminados."}

    @classmethod
    def delete_expired_tokens(cls):
        """Eliminar tokens vencidos automáticamente."""
        sql = """
        DELETE FROM tokens
        WHERE expired_at <= NOW()
        """
        DatabaseConnection.execute_query(sql)
        return {"message": "Tokens expirados eliminados correctamente"},200
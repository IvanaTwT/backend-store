from ..database import DatabaseConnection
from ..models.cliente_model import Cliente
from ..models.product_model import Producto

class Valoracion:
    def __init__(self, **kwargs):
        self.id_valoracion = kwargs.get("id_valoracion")
        self.id_cliente = kwargs.get("id_cliente")
        self.id_producto = kwargs.get("id_producto")
        self.calificacion = kwargs.get("calificacion")
        self.estrellas = kwargs.get("estrellas")
        self.comentario = kwargs.get("comentario")

    def serialize(self):
        return {
            "id_valoracion": self.id_valoracion,
            "id_cliente": self.id_cliente,
            "id_producto": self.id_producto,
            "calificacion": self.calificacion,
            "estrellas": self.estrellas,
            "comentario": self.comentario
        }

    def serialize_with_relations(self):
        return {
            "id_valoracion": self.id_valoracion,
            "cliente": Cliente.get_data_client(self.id_cliente),
            "producto": Producto.get_data_producto(self.id_producto),
            "calificacion": self.calificacion,
            "estrellas": self.estrellas,
            "comentario": self.comentario
        }

    # ---------- CRUD ----------
    @classmethod
    def create(cls, valoracion):
        sql = """INSERT INTO valoracion(id_cliente, id_producto, calificacion, estrellas, comentario)
                 VALUES (%(id_cliente)s, %(id_producto)s, %(calificacion)s, %(estrellas)s, %(comentario)s)"""
        params = valoracion.__dict__
        cursor = DatabaseConnection.execute_query(query=sql, params=params)
        if cursor:
            return cursor.lastrowid
        return None

    @classmethod
    def get(cls, id_valoracion):
        sql = "SELECT * FROM valoracion WHERE id_valoracion=%s"
        result = DatabaseConnection.fetch_one(query=sql, params=(id_valoracion,))
        if result:
            return Valoracion(
                id_valoracion=result[0],
                id_cliente=result[1],
                id_producto=result[2],
                calificacion=result[3],
                estrellas=result[4],
                comentario=result[5]
            )
        return None

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM valoracion"
        results = DatabaseConnection.fetch_all(query=sql)
        valoraciones = []
        if results:
            for v in results:
                valoracion = Valoracion(
                    id_valoracion=v[0],
                    id_cliente=v[1],
                    id_producto=v[2],
                    calificacion=v[3],
                    estrellas=v[4],
                    comentario=v[5]
                ).serialize()
                valoraciones.append(valoracion)
        return valoraciones
    
    @classmethod
    def get_all_by_product(cls,id_producto):
        sql = "SELECT * FROM valoracion WHERE id_producto=%s"
        results = DatabaseConnection.fetch_all(query=sql,params=(id_producto,))
        valoraciones = []
        if results:
            for v in results:
                valoracion = Valoracion(
                    id_valoracion=v[0],
                    id_cliente=v[1],
                    id_producto=v[2],
                    calificacion=v[3],
                    estrellas=v[4],
                    comentario=v[5]
                ).serialize()
                valoraciones.append(valoracion)
        return valoraciones

    @classmethod
    def update(cls, valoracion):
        sql = """UPDATE valoracion 
                 SET calificacion=%(calificacion)s, estrellas=%(estrellas)s, comentario=%(comentario)s
                 WHERE id_valoracion=%(id_valoracion)s"""
        DatabaseConnection.execute_query(query=sql, params=valoracion.__dict__)

    @classmethod
    def delete(cls, valoracion):
        sql = "DELETE FROM valoracion WHERE id_valoracion=%(id_valoracion)s"
        DatabaseConnection.execute_query(query=sql, params=valoracion.__dict__)

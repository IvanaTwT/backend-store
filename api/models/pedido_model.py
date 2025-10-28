from ..database import DatabaseConnection
from flask import session, request, jsonify

class Pedido:
    def __init__(self,**kwargs):
        self.id_pedido = kwargs.get('id_pedido')
        self.id_cliente = kwargs.get('id_cliente')
        self.id_domicilio= kwargs.get("id_domicilio")
        self.fecha = kwargs.get('fecha')
        self.total = kwargs.get('total')
        self.estado = kwargs.get('estado')#'pendiente','pagado','cancelado'
        
    def serialize(self):
        return {
            'id_pedido': self.id_pedido,
            "id_cliente": self.id_cliente,
            "id_domicilio":self.id_domicilio,
            "fecha": self.fecha,
            "total": self.total,
            "estado": self.estado
        }
    
    @classmethod
    def get(cls,id_cliente):
        """Obtiene un pedido por ID cliente."""
        sql="SELECT id_pedido, id_cliente, id_domicilio, fecha, total, estado FROM pedido WHERE id_cliente=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_cliente,))
        
        if result:
            return Pedido(
                id_pedido=result[0],
                id_cliente=result[1],
                id_domicilio=result[2],
                fecha=result[3],
                total=result[4],
                estado=result[5]
            )
        return None
    
    @classmethod
    def get_all_pedidos(cls, id_cliente):
        """Obtiene todos los pedidos de un cliente."""
        sql="SELECT id_pedido, id_cliente, id_domicilio, fecha, total, estado FROM pedido WHERE id_cliente=%s"

        result= DatabaseConnection.fetch_all(query=sql,params=(id_cliente,))
        pedidos=[]
        if result:
            for res in result:
                pedido= Pedido(
                    id_pedido=res[0],
                    id_cliente=res[1],
                    id_domicilio=res[2],
                    fecha=res[3],
                    total=res[4],
                    estado=res[5]
                ).serialize()
                pedidos.append(pedido)
            return pedidos
        return None
    
    @classmethod
    def get_by_id(cls,id_pedido):
        """Obtiene un pedido por su ID."""
        sql="SELECT id_pedido, id_cliente, id_domicilio, fecha, total, estado FROM pedido WHERE id_pedido=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_pedido,))
        
        if result:
            return Pedido(
                id_pedido=result[0],
                id_cliente=result[1],
                id_domicilio=result[2],
                fecha=result[3],
                total=result[4],
                estado=result[5]
            ).serialize()
        return None
    
    @classmethod
    def get_all(cls):
        """Obtiene todos los pedidos."""
        sql="""SELECT id_pedido, id_cliente, id_domicilio, fecha, total, estado FROM pedido"""
        
        results= DatabaseConnection.fetch_all(query=sql)
        
        pedidos=[]
        if results:
            for result in results:
                pedido= Pedido(
                    id_pedido=result[0],
                    id_cliente=result[1],
                    id_domicilio=result[2],
                    fecha=result[3],
                    total=result[4],
                    estado=result[5]
                ).serialize()
                pedidos.append(pedido)
            return pedidos
        return None
    
    @classmethod
    def create(cls,pedido):
        """Crea un nuevo pedido, pasar-> id_cliente,id_domicilio total, estado"""
        sql="INSERT INTO pedido(id_cliente,id_domicilio, total, estado) VALUES (%(id_cliente)s,%(id_domicilio)s, %(total)s, %(estado)s);"
        
        cursor= DatabaseConnection.execute_query(query=sql,params=pedido.__dict__)
        
        if cursor:
            return cursor.lastrowid
        return None
    
    @classmethod
    def update_estado(cls,pedido):
        """SOLO SE VA A PODER MODIFICAR EL ESTADO DEL PEDIDO, MAS ADELANTE LA FECHA"""
        sql="UPDATE pedido SET estado=%(estado)s WHERE id_pedido=%(id_pedido)s;"
        
        DatabaseConnection.execute_query(query=sql,params=pedido.__dict__)
    
    @classmethod
    def update_total(cls,pedido):
        """SOLO SE VA A PODER MODIFICAR EL ESTADO DEL PEDIDO, MAS ADELANTE LA FECHA, pasar total y id"""
        sql="UPDATE pedido SET total=%(total)s WHERE id_pedido=%(id_pedido)s;"
        
        DatabaseConnection.execute_query(query=sql,params=pedido.__dict__)
        
    @classmethod
    def delete(cls,pedido):
        """Elimina un pedido."""
        sql="DELETE FROM pedido WHERE id_pedido=%(id_pedido)s;"
        
        DatabaseConnection.execute_query(query=sql,params=pedido.__dict__)
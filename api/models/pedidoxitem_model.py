from ..database import DatabaseConnection
from datetime import datetime
from flask import session, request, jsonify
from ..models.pedido_model import Pedido
class PedidoXItem:
    def __init__(self,**kwargs):
        self.id_pedidoxitem = kwargs.get('id_pedidoxitem')
        self.id_pedido = kwargs.get('id_pedido')
        self.id_producto= kwargs.get('id_producto')
        self.cantidad = kwargs.get('cantidad')
        self.precioxunidad = kwargs.get('precioxunidad')
        
    def serialize(self):
        return {
            "id_pedidoxitem":self.id_pedidoxitem,
            "id_pedido":self.id_pedido,
            "id_producto":self.id_producto,
            "cantidad":self.cantidad,
            "precioxunidad":self.precioxunidad
        }
    
    @classmethod
    def create(cls,pedido):
        """Agrega un item a un pedido, pasar -> id_pedido, id_producto, cantidad, precioxunidad"""
        sql="""INSERT INTO pedidoxitem(id_pedido, id_producto, cantidad, precioxunidad) 
        VALUES (%(id_pedido)s, %(id_producto)s, %(cantidad)s, %(precioxunidad)s);"""
        
        cursor= DatabaseConnection.execute_query(query=sql,params=pedido.__dict__)
        
        if cursor:
            return cursor.lastrowid
        return None
    
    @classmethod
    def get(cls,id_pedidoxitem):
        """Obtiene un item por su ID."""
        sql="SELECT * FROM pedidoxitem WHERE id_pedidoxitem=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_pedidoxitem,))
        
        if result:
            return PedidoXItem(
                id_pedidoxitem=result[0],
                id_pedido=result[1],
                id_producto=result[2],
                cantidad=result[3],
                precioxunidad=result[4]
            )
        return None
    
    @classmethod
    def get_items_by_pedido(cls,id_pedido):
        """Obtiene los items de un pedido por ID del PEDIDO."""
        sql="SELECT * FROM pedidoxitem WHERE id_pedido=%s"

        results=DatabaseConnection.fetch_all(query=sql,params=(id_pedido,))        
        items = []
        total=0
        if results:
            for result in results:
                item= PedidoXItem(
                    id_pedidoxitem=result[0],
                    id_pedido=result[1],
                    id_producto=result[2],
                    cantidad=result[3],
                    precioxunidad=result[4]
                ).serialize()
                total+=item["precioxunidad"]*item["cantidad"]
                items.append(item)
            Pedido.update_total(Pedido(id_pedido=item["id_pedido"],total=total))
            return items
        return None
    #METODOS DE CLASE QUE PUEDEN SER REALIZADOS SOLO POR UN ADMINISTRADOR
    @classmethod
    def update_item(cls,item):
        """Se podra actualizar la cantidad de un item en un pedido, solo el ADMIN, pasarid pedido, cantidad, id pedidoxitem"""
        sql="""UPDATE pedidoxitem SET cantidad=%(cantidad)s WHERE id_pedido=%(id_pedido)s AND id_pedidoxitem=%(id_pedidoxitem)s;"""
        DatabaseConnection.execute_query(query=sql,params=item.__dict__)
        return item.id_pedidoxitem
        
    @classmethod
    def delete_item(cls,item):
        """Elimina un item de un pedido, solo el ADMIN"""
        sql="DELETE FROM pedidoxitem WHERE id_pedido=%(id_pedido)s AND id_pedidoxitem=%(id_pedidoxitem)s;"
        
        DatabaseConnection.execute_query(query=sql,params=item.__dict__)
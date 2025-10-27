from ..database import DatabaseConnection
#carritoXitem
class CarritoXItem:
    def __init__(self,**kwargs):
        self.id_cartxitem = kwargs.get('id_cartxitem')
        self.id_carrito = kwargs.get('id_carrito')
        self.id_producto= kwargs.get('id_producto')
        self.cantidad = kwargs.get('cantidad')
        
    def serialize(self):
        return {
            'id_cartxitem': self.id_cartxitem,
            "id_carrito": self.id_carrito,
            "id_producto": self.id_producto,
            "cantidad": self.cantidad
        }
        
    @classmethod
    def get_items_by_cart(cls,cart):
        """Obtiene los items de un carrito por ID del CARRITO."""
        sql="SELECT * FROM carritoxitem WHERE id_carrito=%(id_carrito)s"
        
        results=DatabaseConnection.fetch_all(query=sql,params=cart.__dict__)        
        items = []
        for result in results:
            item= CarritoXItem(
                id_cartxitem=result[0],
                id_carrito=result[1],
                id_producto=result[2],
                cantidad=result[3]
            ).serialize()
            items.append(item)
        return items
    
    @classmethod
    def add_item(cls,carritoxitem):
        """Agrega un item a un carrito"""
        sql="INSERT INTO carritoxitem(id_carrito, id_producto, cantidad) VALUES (%(id_carrito)s, %(id_producto)s, %(cantidad)s);"
        
        cursor= DatabaseConnection.execute_query(query=sql,params=carritoxitem.__dict__)
        
        if cursor:
            return cursor.lastrowid
        return None
    
    @classmethod
    def update_item(cls,carritoxitem):
        """Actualiza la cantidad de un producto(item) en un carrito"""
        sql="UPDATE carritoxitem SET cantidad=%(cantidad)s WHERE id_carrito=%(id_carrito)s AND id_cartxitem=%(id_cartxitem)s;"
        
        DatabaseConnection.execute_query(query=sql,params=carritoxitem.__dict__)

    
    @classmethod
    def remove_item(cls,carritoxitem):
        """Elimina un item de un carrito"""
        sql="DELETE FROM carritoxitem WHERE id_carrito=%(id_carrito)s AND id_cartxitem=%(id_cartxitem)s;"
        
        DatabaseConnection.execute_query(query=sql,params=carritoxitem.__dict__)
        
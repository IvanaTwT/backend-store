from ..database import DatabaseConnection

class Carrito:
    def __init__(self,**kwargs):
        self.id_carrito = kwargs.get('id_carrito')
        self.id_cliente = kwargs.get('id_cliente')
        self.fecha = kwargs.get('fecha')
        
    def serialize(self):
        return {
            'id_carrito': self.id_carrito,
            "id_cliente": self.id_cliente,
            "fecha": self.fecha
        }
        
    @classmethod
    def get_cart(cls,cart):
        """Obtiene un carrito por ID del CLIENTE."""
        sql="SELECT * FROM carrito WHERE id_cliente=%(id_cliente)s"
        
        result=DatabaseConnection.fetch_one(query=sql,params=cart.__dict__)
        
        if result:
            return Carrito(
                id_carrito=result[0],
                id_cliente=result[1],
                fecha=result[2]
            )
        return None
    
    @classmethod
    def exist(cls,id_carrito):
        """Verifica si un carrito existe por su id"""
        sql="SELECT * FROM carrito WHERE id_carrito=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_carrito,))
        if result:
            return result
        return None
    
    @classmethod
    def get_all(cls):
        """OBTENER TODOS LOS CARRITOS"""
        sql="SELECT * FROM carrito"
        
        results=DatabaseConnection.fetch_all(sql)
        
        carritos = []
        for result in results:
            cart=Carrito(
                id_carrito=result[0],
                id_cliente=result[1],
                fecha=result[2]
            ).serialize()
            carritos.append(cart)
        return carritos
    
    @classmethod
    def create(cls,cart):
        """Crea un nuevo carrito al crear un usuario cliente, en caso de que el cliente ya tenga un carrito
            que devuelva su id"""
        carrito=Carrito.get_cart(cart)
        print(type(cart))
        if carrito:
            if carrito.id_cliente == cart.id_cliente:
                return carrito.id_carrito
        else:
            sql="INSERT INTO carrito(id_cliente) VALUE(%(id_cliente)s);"
        
            cursor= DatabaseConnection.execute_query(query=sql,params=cart.__dict__)
            
            if cursor:
                return cursor.lastrowid
            return None
    
    @classmethod
    def update(cls,cart):
        """Actualiza fecha y usuario de un carrito por su ID
        si el ADMIN quiere cambiar el carrito de un cliente que ya no usa y que ya existe a otro cliente que no tiene carrito"""
        # print(cart)#object
        carrito=Carrito.exist(cart.id_carrito)
        # print("--------------------",carrito,"--------------------")#tupla
        if carrito:
            if carrito[1] != cart.id_cliente:
                sql="UPDATE carrito SET id_cliente=%(id_cliente)s WHERE id_carrito=%(id_carrito)s"
                DatabaseConnection.execute_query(query=sql,params=cart.__dict__)
                return True
            return False
        return False
        
           
    @classmethod
    def delete(cls,cart):
        """Elimina un carrito por ID del CLIENTE."""
        
        sql="DELETE FROM carrito WHERE id_cliente=%(id_cliente)s"
                
        cursor= DatabaseConnection.execute_query(query=sql,params=cart.__dict__)
        
    @classmethod
    def delete_items(cls,cart):
        """Elimina los items de un carrito por su ID """
        
        sql="DELETE FROM carritoxitem WHERE id_carrito=%(id_carrito)s"
                
        cursor= DatabaseConnection.execute_query(query=sql,params=cart.__dict__)
            
from ..database import DatabaseConnection
from ..models.categoria_model import Categoria
class Producto:
    def __init__(self, **kwargs):
        self.id_producto = kwargs.get('id_producto')
        self.user_id= kwargs.get('user_id')
        self.id_categoria=kwargs.get('id_categoria')# tiene el nombre, marca y descripcion        
        self.path_image=kwargs.get('path_image')#ruta de imagen
        self.color=kwargs.get('color')
        self.precio = kwargs.get('precio', 0.0)
        self.stock = kwargs.get('stock', 0)
        self.talle=kwargs.get('talle')
        self.categoria_edad= kwargs.get('categoria_edad')
        
    def serialize(self):
        return {
            "id_producto":self.id_producto,
            "user_id":self.user_id,
            "id_categoria":self.id_categoria,
            "path_image":self.path_image,
            "color":self.color,
            "precio":self.precio,
            "stock":self.stock,
            "talle":self.talle,
            "categoria_edad":self.categoria_edad,
        }
        
    def serialize_with_categoria(self):
        return {
            "id_producto":self.id_producto,
            "user_id":self.user_id,
            "id_categoria": Categoria.get(self.id_categoria).serialize() if self.id_categoria else None,
            "path_image":self.path_image,
            "color":self.color,
            "precio":self.precio,
            "stock":self.stock,
            "talle":self.talle,
            "categoria_edad":self.categoria_edad,
        }
    @classmethod
    def create(cls,producto):
        sql="""INSERT INTO producto(user_id,id_categoria,path_image,color,precio,stock,talle,categoria_edad)
            VALUES(%(user_id)s,%(id_categoria)s,%(path_image)s,%(color)s,%(precio)s,%(stock)s,%(talle)s,%(categoria_edad)s)
            """
        params=producto.__dict__
        cursor= DatabaseConnection.execute_query(query=sql,params=params)
        
        if cursor:
            return cursor.lastrowid
        return None
    
    @classmethod
    def get(cls, id_producto):
        """DEVUELVE LOS DATOS DE UN PRODUCTO POR EL ID PASADO POR PARAMETRO"""
        sql="SELECT*FROM producto WHERE id_producto=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_producto,))
        
        if result:
            return Producto(
                id_producto=result[0],
                user_id=result[1],
                id_categoria=result[2],
                path_image=result[3],
                color=result[4],
                precio=result[5],
                stock=result[6],
                talle=result[7],
                categoria_edad=result[8]
            )
        return None
    
    @classmethod
    def get_all(cls):
        """DEVUELVE TODOS LOS PRODUCTOS"""
        sql="SELECT*FROM producto"
        
        result= DatabaseConnection.fetch_all(query=sql)
        
        productos=[]
        if result:
            for prod in result:
                producto= Producto(
                    id_producto=prod[0],
                    user_id=prod[1],
                    id_categoria=prod[2],
                    path_image=prod[3],
                    color=prod[4],
                    precio=prod[5],
                    stock=prod[6],
                    talle=prod[7],
                    categoria_edad=prod[8]
                ).serialize_with_categoria()
                productos.append(producto)
            return productos
        return None
    
    @classmethod
    def update(cls,producto):
        """ACTUALIZA UN PRODUCTO"""
        # cambiar de categoria 
        
        sql="UPDATE producto SET "
        producto=producto.__dict__
        for clave,valor in producto.items():
            if clave!="id_producto" and clave!="user_id" and valor:
                sql+=clave+"='"+str(valor)+"', "
            
        sql = sql.rstrip(", ")# # elimina la última coma y espacio
        sql+=" WHERE id_producto = %(id_producto)s"
        print("mensaje SQL ",sql)
        DatabaseConnection.execute_query(query=sql,params=producto)
        
    @classmethod
    def delete(cls,producto):
        """ELIMINACION DE UN PRODUCTO"""
        sql="DELETE from producto WHERE id_producto=%s"
        
        DatabaseConnection.execute_query(query=sql,params=(producto.id_producto,))
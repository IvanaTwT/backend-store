from ..database import DatabaseConnection
from .user_model import Usuario
class Cliente:
    def __init__(self,**kwargs):
        self.id_cliente = kwargs.get('id_cliente')
        self.user_id= kwargs.get('user_id')
        self.nombre_completo = kwargs.get('nombre_completo')
        self.n_celular = kwargs.get('n_celular')

    def serialize(self):
        return {
            "id_cliente": self.id_cliente,
            "user_id":Usuario.get_by_id(self.user_id).serialize(),
            "nombre_completo": self.nombre_completo,
            "n_celular": self.n_celular
        }
        
    @classmethod
    def get_clients(cls):
        """Traer todos los usuarios"""
        sql="SELECT id_cliente, user_id,nombre_completo, n_celular FROM ecommerce.cliente"
        
        result= DatabaseConnection.fetch_all(query=sql)
        
        clientes=[]
        
        if result:
            for client in result:                
                cliente= Cliente(
                                id_cliente = client[0],
                                user_id = client[1],                        
                                nombre_completo = client[2],
                                n_celular= client[3]
                            ).__dict__
                clientes.append(cliente)
            return clientes
        return None
    
    @classmethod
    def get_data_client(cls,id_cliente):
        """Obtener datos del cliente por su id"""
        sql="SELECT*FROM cliente WHERE id_cliente= %s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_cliente,))
        
        if result:
            return Cliente(
                id_cliente=result[0],
                user_id=result[1],
                nombre_completo=result[2],
                n_celular=result[3]
            )
        
        return None
    
    @classmethod    
    def get_client_by_userid(cls,user_id):
        """traer datos del cliente por el id del usuario """
        sql="""SELECT id_cliente, nombre_completo, n_celular
        FROM ecommerce.cliente
        JOIN usuario AS u ON cliente.user_id=u.user_id
        WHERE u.user_id=%s;"""
        result = DatabaseConnection.fetch_one(query=sql, params=(user_id,))
        
        if result:
            return {              
                "id_cliente": result[0],
                "user_id": Usuario.get_by_id(user_id).serialize(),
                "nombre_completo": result[1],
                "n_celular": result[2]
                }
            
        return None
        
    @classmethod
    def get_only_id(cls,user_id):
        """obtener solo el id"""
        sql="""SELECT id_cliente
        FROM ecommerce.cliente
        JOIN usuario AS u ON cliente.user_id=u.user_id
        WHERE u.user_id=%s;"""
        result = DatabaseConnection.fetch_one(query=sql, params=(user_id,))
        
        if result:
            return result[0]
        return None
        
    @classmethod
    def create_client(cls,cliente):
        sql="""INSERT INTO cliente(user_id, nombre_completo,n_celular)
        VALUES(%(user_id)s,%(nombre_completo)s,%(n_celular)s)"""
        params=cliente.__dict__
        cursor= DatabaseConnection.execute_query(query=sql,params=params)
        if cursor:
            return cursor.lastrowid
        return None

    @classmethod
    def update(cls, cliente):
        id=cliente.id_cliente        
        
        if cliente.n_celular:       
            sql="UPDATE cliente SET "
            sql+=" n_celular='"+cliente.n_celular+"'"
            sql= sql.rstrip(", ")# # elimina la última coma
            sql+=" WHERE id_cliente = '%s'"
            print("SQL ",sql)
            DatabaseConnection.execute_query(query=sql,params=(id,))
        if cliente.nombre_completo:       
            sql="UPDATE cliente SET "
            sql+="nombre_completo='"+cliente.nombre_completo+"'"
            sql = sql.rstrip(", ")# # elimina la última coma
            sql+=" WHERE id_cliente = '%s'"
            print("SQL ",sql)
            DatabaseConnection.execute_query(query=sql,params=(id,))
            
    @classmethod
    def delete(cls,usuario):
        sql="""DELETE FROM cliente WHERE user_id= %(user_id)s"""
        DatabaseConnection.execute_query(query=sql,params=usuario.__dict__)
    
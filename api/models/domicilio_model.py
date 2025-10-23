from ..database import DatabaseConnection
from ..models.cliente_model import Cliente
class Domicilio:
    def __init__(self,**kwargs):
        self.id_domicilio = kwargs.get('id_domicilio')
        self.id_cliente=kwargs.get('id_cliente')
        self.domicilio=kwargs.get('domicilio')
        self.ciudad=kwargs.get('ciudad',"Salta Capital")
        self.codigo_postal=kwargs.get("codigo_postal","4400")
    
    def serialize(self):
        return {
            "id_domicilio":self.id_domicilio,
            "id_cliente":self.id_cliente,
            "domicilio":self.domicilio,
            "ciudad":self.ciudad,
            "codigo_postal":self.codigo_postal
        }
        
    def serialize_with_client(self):
        return {
            "id_domicilio":self.domicilio,
            "id_cliente":Cliente.get_data_client(self.id_cliente),
            "domicilio":self.domicilio,
            "ciudad":self.ciudad,
            "codigo_postal":self.codigo_postal
        }
    @classmethod
    def create(cls,domicilio):
        """CREAR DOMICILIO, pasar id_cliente, domicilio,ciudad),odigo_postal"""
        sql="""INSERT INTO domicilio(id_cliente,domicilio,ciudad,codigo_postal)
            VALUES(%(id_cliente)s,%(domicilio)s,%(ciudad)s,%(codigo_postal)s)"""
            
        params=domicilio.__dict__
        
        cursor= DatabaseConnection.execute_query(query=sql,params=params)
        
        if cursor:
            return cursor.lastrowid
        return None
    
    @classmethod
    def get(cls, id_cliente):
        """TRAER DOMICILIO por id del CLIENTE"""
        sql="SELECT*FROM domicilio WHERE id_cliente=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_cliente,))
        
        if result:
            return Domicilio(
                id_domicilio=result[0],
                id_cliente=result[1],
                domicilio=result[2],
                ciudad=result[3],
                codigo_postal=result[4]
            )
        return None
    @classmethod
    def get_all_domicilios(cls,id_cliente):
        """DEVUELVE UNA LISTA DE LOS DOMICILIOS QUE TIENE EL CLIENTE"""
        sql="SELECT id_domicilio, id_cliente, domicilio, ciudad, codigo_postal FROM domicilio WHERE id_cliente=%s"
        
        result= DatabaseConnection.fetch_all(query=sql,params=(id_cliente,))
        
        domicilios=[]
        # print(len(result))
        if result and len(result)<2:
            result=result[0]
            return Domicilio(
                id_domicilio=result[0],
                id_cliente=result[1],
                domicilio=result[2],
                ciudad=result[3],
                codigo_postal=result[4]
            )
        elif result and len(result)>1:
            for domi in result:
                domicilio=Domicilio(
                id_domicilio=domi[0],
                id_cliente=domi[1],
                domicilio=domi[2],
                ciudad=domi[3],
                codigo_postal=domi[4]
                ).serialize()
                domicilios.append(domicilio)
            return domicilios
        
        return None
        
        
    @classmethod
    def get_id(cls,id_cliente):
        """DEVUELVE EL ID DEL DOMICILIO"""
        sql="SELECT id_domicilio FROM domicilio WHERE id_cliente=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_cliente,))
        
        if result:
            return result[0]
        return None
        pass
    
    @classmethod
    def get_domicilio(cls,id_domicilio):
        """TRAER los datos por un id_domicilio"""
        sql="SELECT*FROM domicilio WHERE id_domicilio=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_domicilio,))
        
        if result:
            return Domicilio(
                id_domicilio=result[0],
                id_cliente=result[1],
                domicilio=result[2],
                ciudad=result[3],
                codigo_postal=result[4]
            )
        return None
    
    @classmethod
    def update(cls,domicilio):
        """actualizar domicilio, pasar domicilio, id y el id del cliente"""
        sql="""UPDATE ecommerce.domicilio
            SET domicilio=%(domicilio)s WHERE id_domicilio=%(id_domicilio)s and id_cliente=%(id_cliente)s"""
        
        DatabaseConnection.execute_query(query=sql,params=domicilio.__dict__)
    
    @classmethod
    def delete(cls,domicilio):
        """eliminar domicilio, pasar id_domicilio""" 
        sql="""DELETE FROM domicilio WHERE id_domicilio= %(id_domicilio)s"""
        DatabaseConnection.execute_query(query=sql,params=domicilio.__dict__)
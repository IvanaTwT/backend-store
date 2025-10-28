from ..database import DatabaseConnection
class Pago:
    def __init__(self, **kwargs):
        self.id_pago=kwargs.get("id_pago")
        self.id_pedido=kwargs.get("id_pedido")
        self.metodo=kwargs.get("metodo") # metodo ENUM("mercado pago","efectivo","50-50"),
        self.monto=kwargs.get("monto")
        self.estado=kwargs.get("estado")# estado ENUM("pendiente","exitoso","fallido"),
        self.fecha=kwargs.get("fecha")
        
    def serialize(self):
        return {
            "id_pago": self.id_pago,
            "id_pedido": self.id_pedido,
            "metodo": self.metodo,
            "monto": self.monto,
            "estado": self.estado,
            "fecha": self.fecha
        }
    
    @classmethod
    def create(cls,pago):
        """ Crea un nuevo pago en la base de datos. pasar-> id_pedido,metodo,monto,estado"""
        sql="""INSERT INTO pago (id_pedido, metodo, monto, estado) 
               VALUES (%(id_pedido)s, %(metodo)s, %(monto)s, %(estado)s)"""
        
        cursor= DatabaseConnection.execute_query(query=sql,params=pago.__dict__)
        
        if cursor:
            return cursor.lastrowid
        return None
    
    @classmethod
    def get_by_id(cls,id_pago):
        """Obtiene un pago por su ID."""
        sql="SELECT id_pago, id_pedido, metodo, monto, estado, fecha FROM pago WHERE id_pago=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_pago,))
        
        if result:
            return Pago(
                id_pago=result[0],
                id_pedido=result[1],
                metodo=result[2],
                monto=result[3],
                estado=result[4],
                fecha=result[5]
            )
        return None
    
    @classmethod
    def get_by_pedido_id(cls,id_pedido):
        """Obtiene un pago por el ID del pedido asociado."""
        sql="SELECT id_pago, id_pedido, metodo, monto, estado, fecha FROM pago WHERE id_pedido=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_pedido,))
        
        if result:
            return Pago(
                id_pago=result[0],
                id_pedido=result[1],
                metodo=result[2],
                monto=result[3],
                estado=result[4],
                fecha=result[5]
            ).serialize()
        return None
    
    @classmethod
    def get_all(cls):
        """Obtiene todos los pagos."""
        sql="""SELECT id_pago, id_pedido, metodo, monto, estado, fecha FROM pago"""
        pagos=[]
        
        results= DatabaseConnection.fetch_all(query=sql)
        
        if results:
            for result in results:
                pago= Pago(
                    id_pago=result[0],
                    id_pedido=result[1],
                    metodo=result[2],
                    monto=result[3],
                    estado=result[4],
                    fecha=result[5]
                ).serialize()
                pagos.append(pago)
            return pagos        
        return None
    
    #metodos de actualizar y eliminar que requieren del administrador para ser corrigas
    @classmethod
    def update(cls, pago):
        """ACTUALIZAR METODO O ESTADO DE PAGO. pasar-> id_pago, metodo, estado"""
        sql="UPDATE pago SET "
        #metodo=%(metodo)s, estado=%(estado)s WHERE id_pago=%(id_pago)s
        if pago.metodo:
            sql+="metodo=%(metodo)s ,"
        
        if  pago.estado:
            sql+=" estado=%(estado)s ,"
        
        if pago.metodo=="" and pago.estado=="":
            return None
        sql = sql.rstrip(", ")
        sql+=" WHERE id_pago=%(id_pago)s"
        DatabaseConnection.execute_query(query=sql,params=pago.__dict__)
        
        return True
    
    @classmethod
    def update_monto(cls, pago):
        """actualizar monto"""
        sql="UPDATE pago SET monto= %(monto)s WHERE id_pago=%(id_pago)s"
        DatabaseConnection.execute_query(query=sql,params=pago.__dict__)
    
    @classmethod
    def delete(cls,pago):
        """Elimina un pago por su ID."""
        sql="DELETE FROM pago WHERE id_pago=%(id_pago)s"
        DatabaseConnection.execute_query(query=sql,params=pago.__dict__)
        
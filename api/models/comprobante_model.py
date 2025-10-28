from ..database import DatabaseConnection
from ..models.pago_model import Pago
class Comprobante:
    def __init__(self, **kwargs):
        self.id_comprobante=kwargs.get("id_comprobante")
        self.id_pago=kwargs.get("id_pago")
        #self.tipo=kwargs.get("tipo") # tipo ENUM("factura","recibo","boleta"),
        self.n_comprobante=kwargs.get("n_comprobante")
        self.fecha=kwargs.get("fecha")
        # self.importe=kwargs.get("importe")
        
        
    def serialize(self):
        return {
            "id_comprobante": self.id_comprobante,
            "id_pago": self.id_pago,
            #"tipo": self.tipo,
            "n_comprobante": self.n_comprobante,
            "fecha": self.fecha,
            # "importe": self.importe
        }
    
    def serialize_with_pago(self):
        return {
            "id_comprobante": self.id_comprobante,
            "id_pago": Pago.get_by_id(self.id_pago) ,
            "n_comprobante": self.n_comprobante,
            "fecha": self.fecha,
            # "importe": self.importe
        }
        
    @classmethod
    def next_comprobante(cls,actual=None):
        if not actual:
            return "A-000-001"
        
        letras, medio, ultimo = actual.split("-")
        medio, ultimo = int(medio), int(ultimo)

        ultimo += 1
        if ultimo > 999:
            ultimo = 0
            medio += 1
            if medio > 999:
                medio = 0
                # si querés que cambie la letra, la incrementás aquí
                letras = chr(ord(letras) + 1)
                
        
        
        return f"{letras}-{medio:03d}-{ultimo:03d}"
    
    @classmethod
    def last_n_comprobante(cls):
        """traer el ultimo numero de comprobante"""
        sql="SELECT n_comprobante FROM comprobante"        
        #"pendiente","exitoso","fallido
        result= DatabaseConnection.fetch_all(query=sql)
        
        if result:
            ultimo_valor=result[len(result)-1]
            return ultimo_valor
        return None
        
        
    @classmethod
    def create(cls, comprobante):
        """Crea un nuevo comprobante en la base de datos."""
        numero_c = Comprobante.last_n_comprobante()
        print("Numero: ", numero_c)

        # si no hay comprobantes previos
        if not numero_c:
            new_numero = Comprobante.next_comprobante(None)
        else:
            new_numero = Comprobante.next_comprobante(numero_c[0])

        comprobante.n_comprobante = new_numero

        sql = """INSERT INTO comprobante (id_pago, n_comprobante) 
                VALUES (%(id_pago)s, %(n_comprobante)s)"""

        cursor = DatabaseConnection.execute_query(query=sql, params=comprobante.__dict__)

        if cursor:
            return cursor.lastrowid
        return None

        
    
    @classmethod
    def get_estado(cls,id_pago):
        """Obtiene el estado del pago"""
        sql="SELECT estado FROM pago WHERE id_pago=%s"        
        #"pendiente","exitoso","fallido
        result= DatabaseConnection.fetch_one(query=sql,params=(id_pago,))
        
        if result:
            return result[0]
        return None
    
    @classmethod
    def get_by_id(cls,id_comprobante):
        """Obtiene un comprobante por su ID."""
        sql="SELECT id_comprobante, id_pago, n_comprobante, fecha FROM comprobante WHERE id_comprobante=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_comprobante,))
        
        if result:
            return Comprobante(
                id_comprobante=result[0],
                id_pago=result[1],
                n_comprobante=result[2],
                fecha=result[3]
            ).serialize_with_pago()
        return None
    
    @classmethod
    def get_by_pago_id(cls,id_pago):
        """Obtiene un comprobante por el ID del pago asociado."""
        sql="SELECT id_comprobante, id_pago, n_comprobante, fecha FROM comprobante WHERE id_pago=%s"
        
        result= DatabaseConnection.fetch_one(query=sql,params=(id_pago,))
        
        if result:
            return Comprobante(
                id_comprobante=result[0],
                id_pago=result[1],
                n_comprobante=result[2],
                fecha=result[3]
            )
        return None

    @classmethod
    def get_all(cls):
        """traer todos los comprobantes"""
        sql="SELECT id_comprobante, id_pago, n_comprobante, fecha FROM comprobante"
        
        results= DatabaseConnection.fetch_all(query=sql)
        
        comprobantes=[]
        if results:
            for result in results:
                comprobante= Comprobante(
                    id_comprobante=result[0],
                    id_pago=result[1],
                    n_comprobante=result[2],
                    fecha=result[3]
                ).serialize()
                comprobantes.append(comprobante)
            return comprobantes
        return None
    
    #metodos de actualizar y eliminar que requieren del administrador para ser corrigas
    @classmethod
    def update(cls, comprobante):
        """ACTUALIZAR fecha"""
        sql="UPDATE comprobante SET "
        #metodo=%(metodo)s, estado=%(estado)s WHERE id_pago=%(id_pago)s
        if comprobante.fecha:
            sql+="fecha=%(fecha)s WHERE id_comprobante=%(id_comprobante)s"      
            DatabaseConnection.execute_query(query=sql,params=comprobante.__dict__)            
            return True
        return False
    
    @classmethod
    def delete(cls,comprobante):
        """Elimina un comprobante por su ID."""
        sql="DELETE FROM comprobante WHERE id_comprobante=%(id_comprobante)s"
        DatabaseConnection.execute_query(query=sql,params=comprobante.__dict__)    
        
from ..database import DatabaseConnection
import hashlib

# Función para generar un hash de una cadena-un proceso criptográfico (contraseña a una cadena de longitud fija)
def hash_string(string):
    return hashlib.sha256(string.encode()).hexdigest()

class Usuario:
    def __init__(self,**kwargs):
        self.user_id = kwargs.get('user_id')
        self.username= kwargs.get('username')
        self.email = kwargs.get('email')
        if (kwargs.get('password')):
            self.password = hash_string(kwargs.get('password'))
        else:
            self.password=kwargs.get('password')
        self.admin=  kwargs.get('admin')
        self.inhabilitado=  kwargs.get('inhabilitado')
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "username":self.username,
            "email": self.email,
            "password": self.password,            
            "admin": self.admin,
            "inhabilitado":self.inhabilitado
        }
    # Función para verificar que el usuario exista en la base de datos
    @classmethod
    def verify_user(self,usuario):
        """
        VERIFICAR QUE EL USUARIO SEA VALIDO (en bd)
        """
        #Comprobar si el usuario se encuentra alojado en la base de datos
        query = """SELECT user_id, username, email, password, admin, inhabilitado FROM ecommerce.usuario 
        WHERE username = %(username)s and password = %(password)s"""
        params = usuario.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        # print(usuario.password==result[3])
        if result:
            return Usuario(
                            user_id = result[0],
                            username = result[1],                        
                            email = result[2],
                            password= result[3],
                            admin = result[4],
                            inhabilitado= result[5]
                        )
        return None
    
    @classmethod
    def get(cls, usuario):
        """Traer a un usuario por su username"""
        sql="""SELECT* FROM ecommerce.usuario WHERE username=%s"""
        result= DatabaseConnection.fetch_one(query=sql, params=(usuario.username,))
        
        if result:
            return Usuario(
                            user_id = result[0],
                            username = result[1],                        
                            email = result[2],
                            password= result[3],
                            admin = result[4],
                            inhabilitado=result[5]
                        )
        return None
    
    @classmethod
    def get_by_id(cls, user_id):
        """Traer a un usuario por su id"""
        sql="""SELECT user_id, username, email, password, admin,inhabilitado FROM ecommerce.usuario WHERE user_id=%s"""
        result= DatabaseConnection.fetch_one(query=sql, params=(user_id,))
        
        if result:
            return Usuario(
                            user_id = result[0],
                            username = result[1],                        
                            email = result[2],
                            password= result[3],
                            admin = result[4],
                            inhabilitado=result[5]
                        )
        return None
    @classmethod
    def get_users(cls):
        """Traer todos los usuarios"""
        sql="SELECT user_id, username, email, password, admin,inhabilitado  FROM ecommerce.usuario"
        
        result= DatabaseConnection.fetch_all(query=sql)
        
        usuarios=[]
        
        if result:
            for user in result:                
                usuario= Usuario(
                                user_id = user[0],
                                username = user[1],                        
                                email = user[2],
                                password= user[3],
                                admin = user[4],
                                inhabilitado=user[5]
                            ).serialize()
                usuarios.append(usuario)
            return usuarios
        return None
    
    @classmethod
    def create(cls,usuario):
        """Crear usuario"""
        sql="""INSERT INTO usuario(username,email,password) 
        VALUES(%(username)s,%(email)s,%(password)s)
        """
        c= DatabaseConnection.execute_query(query=sql, params=usuario.__dict__)
        # result= Usuario.get(Usuario(username=usuario.username))
        
        if c.lastrowid:
            return c.lastrowid
        return None
    
    @classmethod
    def update(cls, usuario):
        id=usuario.user_id
        usuario=usuario.__dict__
        
        sql="UPDATE usuario SET "
        
        for c,v in usuario.items():
            if c=="password" and v:
                pass_hash=hash_string(v)
                sql+=c+"='"+str(pass_hash)+"', "
            if c!="user_id" and v:
                sql+=c+"='"+str(v)+"', "
            
        sql = sql.rstrip(", ")# # elimina la última coma y espacio
        sql+=" WHERE user_id = '%s'"
        print("mensaje SQL ",sql)
        DatabaseConnection.execute_query(query=sql,params=(id,))
        
    @classmethod
    def update_inhabilitado(cls, usuario):
        sql="""UPDATE usuario SET inhabilitado=1 WHERE user_id=%(user_id)s"""
        DatabaseConnection.execute_query(query=sql,params=usuario.__dict__)

    @classmethod
    def delete(cls,usuario):
        sql="""DELETE FROM usuario WHERE user_id= %(user_id)s"""
        DatabaseConnection.execute_query(query=sql,params=usuario.__dict__)
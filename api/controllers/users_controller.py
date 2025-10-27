from ..models.user_model import Usuario, hash_string
from ..models.cliente_model import Cliente
from ..models.carrito_model import Carrito
from config import Config    #traer clave secreta
from flask import request, session, jsonify
import datetime as dt
#importaciones para token
import jwt
from datetime import datetime, timedelta, UTC
from ..models.token_model import Token

class UserController:
    """Clase de controlador de usuarios."""
    
    @classmethod
    def login(cls):
        data = request.json
        user = Usuario(
            username = data.get('username'),
            password = data.get('password')
        )
        # print("USER: ",user.serialize())
        user_verify=Usuario.verify_user(user)
        if user_verify:
            # print("verificado: ",user_verify.serialize())
            if int(user_verify.inhabilitado)==0:
                session['username'] = data.get('username')
                session['admin'] = user_verify.admin
                session['user_id'] = user_verify.user_id
                token_user= Token.get_tokens_by_user(user_verify.user_id)
                # print(type(token_user))
                if(token_user):
                    return jsonify({"token": token_user.token}), 200 
                else:
                    token = Token.create_token(user_verify.user_id)
                    return jsonify({"token": token}), 200 
            else:
                return jsonify({"error":"Usuario dado de baja"}),200
        else:
            return jsonify({"error": "Usuario o contraseña incorrectos"}), 200
        
    @classmethod
    def ver_users(cls):
        usuarios=Usuario.get_users()
        
        if usuarios:
            return {"usuarios":usuarios},200
        
        return {"message":"No hay usuario que mostrar"},400
    
    @classmethod
    def ver_clients(cls):
        clientes=Cliente.get_clients()
        
        if clientes:
            return {"clientes":clientes},200
        
        return {"message":"No hay clientes que mostrar"},400
    
    @classmethod
    def verify_authentication(self):
        auth_credentials = request.authorization
        print(auth_credentials.token)
        if auth_credentials and auth_credentials.type in ["bearer","token"]:
            try:
                token = auth_credentials.token
                payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
                # print(payload){'id_usuario': 4, 'exp': 1737296376}
                # Verificar el token en la base de datos
                db_token= Token.get_token(token)
                if payload:
                    user_id = payload["user_id"]
                    user =Usuario.get_by_id(user_id)
                    if user and db_token:
                        cliente= Cliente.get_client_by_userid(user.user_id)
                        if cliente:
                            return cliente             
                        usuario=Usuario(
                            user_id= user.user_id,
                            username= user.username,
                            email=user.email,
                            admin=user.admin
                            ).serialize()
                        return usuario
                    return None
                return None
            except jwt.ExpiredSignatureError:
                raise Exception("Token vencido")
        return None
 
    
    @classmethod
    def profile(cls):
        user_data = UserController.verify_authentication()
        print("USER: ",user_data)
        # user = Usuario.get(Usuario(username = username))
        # print("USER: ",user)
        if user_data is None :
            return {"error": "Usuario no encontrado"}, 404
        else:
            return jsonify(user_data), 200
    
    @classmethod
    def logout(cls):
        auth_credentials = request.authorization
        if auth_credentials and auth_credentials.type in ["bearer", "token"]:
            session.pop('username', None)
            return {"message": "Sesion cerrada"}, 200
        return {"error": "No se encontró el token"}, 401
        
    @classmethod
    def profile_by_id(cls, user_id):
        """Mostrar perfil de un usuario"""
        if 'username' in session:
            user = Usuario.get_by_id(user_id)
            if user is None:
                return {"message": "Usuario no encontrado"}, 404
            else:
                if (user.admin):
                    return user.serialize(), 200
                else:
                    return Cliente.get_client_by_userid(user.user_id) , 200
        else:
            return {"error":"Inicie Session para ver los perfiles"}, 400
    #Todo lo de arriba todo joya
    @classmethod
    def create_user(cls):
        data = request.json
        #username, email, password, admin
        user = Usuario(**data)
        new_id =Usuario.create(user)
        print("new_id: ",new_id)
        cliente= Cliente(user_id=new_id,**data)
        response = Cliente.create_client(cliente)#devuleve el id creado
        cart= Carrito.create(Carrito(id_cliente=response))
        if response:
            return {"message":"Usuario creado con exito"} ,200   
        return {"error":"Error al crear usuario"},400
    
    @classmethod
    def update_user(cls,user_id):
        print("ID;",user_id)
        """method: PUT, se actualizaran los campos que esten cargados"""
        data = request.json
        #se inicializa el usuario con los campos que esten y tambien cliente
        data["user_id"]=user_id
        
        verify_user= UserController.verify_authentication()
        is_admin=0
        if verify_user["id_cliente"] is not None:
            is_admin= verify_user["user_id"]["admin"]
        else: 
            is_admin= verify_user["admin"] 
            
        if (data and verify_user):            
            usuario=Usuario(**data)            
            if usuario and is_admin==1:
                Usuario.update(usuario)
                return {"message":"Los datos del usuario fueron actualizados correctamente"},200 
            elif usuario and is_admin==0:
                if "username" in data or "email" in data or "password" in data:
                    Usuario.update(usuario)
                if "id_cliente" not in data:
                    data["id_cliente"]= Cliente.get_only_id(user_id)
                    cliente=Cliente(**data)
                    Cliente.update(cliente)
                return {"message":"Los datos fueron actualizados correctamente"},200        
            else:
                return {"error":"No hay campos para actualizar"},400
        else:
            return {"error":"No hay campos para actualizar"},400
        
    @classmethod
    def delete_user(cls,user_id):
        verify_user= UserController.verify_authentication()
        is_admin=verify_user["user_id"]["admin"]
        user=Usuario(user_id=user_id)
        if is_admin and user_id:            
            #solo el administrador puede eliminar usuario en caso de cambiar administrador            
            if Cliente.get_only_id(user.user_id):#si es cliente devuelve el id
                # Cliente.delete(user)
                return {"message":"Cliente dado de baja"},201
            Usuario.update_inhabilitado(user)
            # Usuario.delete(user)
            return {"message":"Usuario dado de baja"},201
        elif user_id == verify_user["user_id"]["user_id"]:
            #en caso de el usuario elimiar su cuenta
            if Cliente.get_only_id(user.user_id):
                Usuario.update_inhabilitado(user)
                # Usuario.delete(user)
                # Cliente.delete(user)                
                return {"message":"Cliente dado de baja"},201
            else: 
                # Usuario.delete(user)
                Usuario.update_inhabilitado(user)
                return {"message":"Usuario dado de baja"},201
        else:
            return {"error":"Error al eliminar usuario"},404
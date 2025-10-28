from flask import Blueprint

from ..controllers.users_controller import UserController

user_bp = Blueprint('user_bp', __name__) #users
#inicio de sesion y perfil
user_bp.route('/login', methods=['POST'])(UserController.login)#login de usuario con nick_name y password
#ver usuarios
user_bp.route('/users', methods=['GET'])(UserController.ver_users)
#ver usuarios-clientes
user_bp.route('/clients', methods=['GET'])(UserController.ver_clients)
#ver perfil de usuario logeado
user_bp.route('/profile', methods=['GET'])(UserController.profile)
#vista del perfil de un usuario por su id 
user_bp.route('/profile/<int:user_id>', methods=['GET'])(UserController.profile_by_id)
user_bp.route('/profile-client/<int:id_cliente>', methods=['GET'])(UserController.profile_by_id_cliente)
user_bp.route('/logout', methods=['GET'])(UserController.logout)#
#CRUD de usuario
user_bp.route("/new_user/", methods=['POST'])(UserController.create_user)
user_bp.route("/update/<int:user_id>", methods=['PUT'])(UserController.update_user)#editar el prerfil del usuario
user_bp.route('/delete/<int:user_id>', methods=["DELETE"])(UserController.delete_user)
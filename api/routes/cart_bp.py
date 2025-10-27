from ..controllers.cart_controller import CartController
from flask import Blueprint

cart_bp = Blueprint('cart_bp', __name__) #users
#mostrar los datos de un carrito
cart_bp.route('/add', methods=['POST'])(CartController.create_cart)
#mostrar los datos de un carrito
cart_bp.route('/<int:id_cliente>', methods=['GET'])(CartController.get_cart)
#mostrar TODOS los carritos
cart_bp.route('/', methods=['GET'])(CartController.get_all_carts)
#update
cart_bp.route('/update', methods=['PUT'])(CartController.update_cart)
#ELIMINAR CARRITO
cart_bp.route('/delete', methods=['DELETE'])(CartController.delete_cart)
#agregar item(un producto) al carrito
cart_bp.route('/add-item', methods=['POST'])(CartController.add_item)
#actualizar cantidad
cart_bp.route('/update-item', methods=['PUT'])(CartController.update_item)
#eliminar item
cart_bp.route('/delete-item', methods=['DELETE'])(CartController.delete_item)
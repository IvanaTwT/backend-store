from flask import Blueprint

from ..controllers.product_controller import ProductController

product_bp = Blueprint('product_bp', __name__) #users
#mostrar categorias
product_bp.route('/categories', methods=['GET'])(ProductController.ver_categorias)
#mostrar UNA categoria
product_bp.route('/categories/<int:id_categoria>', methods=['GET'])(ProductController.ver_categoria)
#mostrar categorias
product_bp.route('/categories/new-categoria', methods=['POST'])(ProductController.create_categoria)
#actualizar categoria
product_bp.route('/update', methods=['PUT'])(ProductController.update_categoria)
#eliminar categoria
product_bp.route('/categories/delete', methods=['DELETE'])(ProductController.delete_categoria)
#desde PRODUCTO
product_bp.route('/product/<int:id_producto>', methods=['GET'])(ProductController.ver_producto)
product_bp.route('/all', methods=['GET'])(ProductController.ver_productos)
#crear
product_bp.route('/new-product', methods=['POST'])(ProductController.create_product)
#update
product_bp.route('/update-product', methods=["PUT"])(ProductController.update_product)
#delete
product_bp.route('/delete-product', methods=["DELETE"])(ProductController.delete_product)
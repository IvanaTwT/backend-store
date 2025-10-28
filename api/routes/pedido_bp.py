from ..controllers.pedido_controller import PedidoController
from flask import Blueprint

pedido_bp= Blueprint("pedido_bp",__name__)

#crear un nuevo pedido
pedido_bp.route('/new',methods=['POST'])(PedidoController.create_pedido)
#crear un nuevo pedido con items
pedido_bp.route('/create',methods=['POST'])(PedidoController.create_pedido_completo)
#ver todos los pedidos
pedido_bp.route('/',methods=['GET'])(PedidoController.get_all_pedidos)
#ver un pedido por id_cliente
pedido_bp.route('/<int:id_cliente>',methods=['GET'])(PedidoController.get_pedido)
#ver TODOS LOS PEDIDOS por id_cliente
pedido_bp.route('/all/<int:id_cliente>',methods=['GET'])(PedidoController.get_all_pedidos_more_items)
#ver un pedido por su id
pedido_bp.route('/by-id/<int:id_pedido>',methods=['GET'])(PedidoController.get_pedido_by_id)
#actualizar estado
pedido_bp.route('/update-estado',methods=['PUT'])(PedidoController.update_estado)
#actualizar total
pedido_bp.route('/update-total',methods=['PUT'])(PedidoController.update_total)
#actualizar estado
pedido_bp.route('/add-pedidoxitem',methods=['POST'])(PedidoController.add_pedidoxitem)
#actualizar cantidad de algun item(producto)
pedido_bp.route('/update-item/cantidad',methods=['PUT'])(PedidoController.update_item)
#delete pedido
pedido_bp.route('/delete',methods=['DELETE'])(PedidoController.delete_pedido)
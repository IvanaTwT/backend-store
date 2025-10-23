from flask import Blueprint

from ..controllers.domicilio_controller import DomicilioController

domi_bp = Blueprint('domi_bp', __name__) #users
#mostrar un domicilio en especifico
domi_bp.route('/<int:id_domicilio>', methods=['GET'])(DomicilioController.get_domicilio)
#mostrar 1 domiclio por  el id_cliente en especifico
domi_bp.route('/client/<int:id_cliente>', methods=['GET'])(DomicilioController.get_domicilio_by_idClient)
# obtener todos los domicilio que cargo el cliente
domi_bp.route('/me/<int:id_cliente>', methods=['GET'])(DomicilioController.get_domicilio_client)
#crear domicilio
domi_bp.route('/', methods=['POST'])(DomicilioController.create_domicilio)
#update domicilio
domi_bp.route('/update', methods=['PUT'])(DomicilioController.update_address)
#delete 
domi_bp.route('/delete/<int:id_domicilio>', methods=['DELETE'])(DomicilioController.delete_address)
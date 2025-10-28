from ..controllers.pago_controller import PagoController

from flask import Blueprint

pago_bp= Blueprint("pago_bp",__name__)

pago_bp.route('/',methods=['GET'])(PagoController.get_all_pagos)
#ver todos los comprobantes
pago_bp.route('/invoices',methods=['GET'])(PagoController.get_all)
pago_bp.route('/<int:id_pago>',methods=['GET'])(PagoController.get_pago_by_id)
#ver por un pedido en particular
pago_bp.route('/pedido/<int:id_pedido>',methods=['GET'])(PagoController.get_pago_by_pedido_id)
pago_bp.route('/new',methods=['POST'])(PagoController.create_pago)
pago_bp.route("/update-amount", methods=["PUT"])(PagoController.update_monto_pago)
pago_bp.route("/update", methods=["PUT"])(PagoController.update_metodo_estado)
#eliminar pago, elimina en cascada sus referencias, si tenia comprobante seran eliminados
pago_bp.route("/delete-pago", methods=["DELETE"])(PagoController.delete_pago)
#crear comprobante, actualizar, eliminar.
pago_bp.route('/new-invoices',methods=['POST'])(PagoController.create_comprobante)
pago_bp.route("/invoices/update-fecha", methods=["PUT"])(PagoController.update_fecha_comprobante)
pago_bp.route("/delete-comprobante", methods=["DELETE"])(PagoController.delete_comprobante)

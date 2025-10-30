from flask import Blueprint
from ..controllers.valo_controller import ValoracionController

valo_bp = Blueprint("valo_bp", __name__)

valo_bp.route("/", methods=["GET"])(ValoracionController.get_valoraciones)
valo_bp.route("/<int:id_valoracion>", methods=["GET"])(ValoracionController.get_valoracion)
valo_bp.route("/product/<int:id_producto>", methods=["GET"])(ValoracionController.get_valoracion_by_product)
valo_bp.route("/", methods=["POST"])(ValoracionController.create_valoracion)
valo_bp.route("/<int:id_valoracion>", methods=["PUT"])(ValoracionController.update_valoracion)
valo_bp.route("/<int:id_valoracion>", methods=["DELETE"])(ValoracionController.delete_valoracion)
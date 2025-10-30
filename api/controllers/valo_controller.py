from config import Config    #traer clave secreta
from flask import request, session, jsonify
from ..models.valoracion_model import Valoracion

class ValoracionController:
    @classmethod
    def get_valoraciones(cls):
        valoraciones = Valoracion.get_all()
        if valoraciones:
            return jsonify({"message":valoraciones}), 200
        return jsonify({"error":"No hay valoraciones para mostrar"}), 400

    @classmethod
    def get_valoracion_by_product(cls,id_producto):
        valoraciones = Valoracion.get_all_by_product(id_producto)
        if valoraciones:
            return jsonify({"message":valoraciones}), 200
        return jsonify({"error":"No hay valoraciones de este producto para mostrar"}), 200
    
    @classmethod
    def get_valoracion(cls,id_valoracion):
        valoracion = Valoracion.get(id_valoracion)
        if not valoracion:
            return jsonify({"error": "Valoración no encontrada"}), 404
        return jsonify({"message":valoracion.serialize()}), 200

    @classmethod
    def create_valoracion(cls):
        data = request.json
        print(data)
        nueva_valoracion = Valoracion(**data)
        id_nueva = Valoracion.create(nueva_valoracion)
        if id_nueva:
            return jsonify({"message": "Valoración creada", "id_valoracion": id_nueva}), 201
        return jsonify({"error": "No se pudo crear la valoración"}), 400

    @classmethod
    def update_valoracion(cls,id_valoracion):
        data = request.json
        valoracion = Valoracion.get(id_valoracion)
        if not valoracion:
            return jsonify({"error": "Valoración no encontrada"}), 404
        
        # actualizar campos
        valoracion.calificacion = data.get("calificacion", valoracion.calificacion)
        valoracion.estrellas = data.get("estrellas", valoracion.estrellas)
        valoracion.comentario = data.get("comentario", valoracion.comentario)

        Valoracion.update(valoracion)
        return jsonify({"message": "Valoración actualizada"}), 200

    @classmethod
    def delete_valoracion(cls,id_valoracion):
        valoracion = Valoracion.get(id_valoracion)
        if not valoracion:
            return jsonify({"error": "Valoración no encontrada"}), 404
        
        Valoracion.delete(valoracion)
        return jsonify({"message": "Valoración eliminada"}), 200
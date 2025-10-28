from flask import session, request, jsonify
from ..models.pago_model import Pago
from ..models.comprobante_model import Comprobante
from ..models.pedido_model import Pedido
from ..models.pedidoxitem_model import PedidoXItem

class PagoController:
    @classmethod
    def get_pago_by_id(cls, id_pago):
        """Obtiene un pago por su ID, junto con su comprobante y los items del pedido asociado."""
        pago= Pago.get_by_id(id_pago)
        if id_pago:
            if pago:
                pedido_items= PedidoXItem.get_items_by_pedido(Pedido(id_pedido=pago.id_pedido))
                comprobante= Comprobante.get_by_pago_id(pago.id_pago)
                if comprobante and pedido_items:
                    return {
                        "pago": pago.serialize(),
                        "comprobante": comprobante.serialize(),
                        "items": [item for item in pedido_items]
                    },200
                return{ "message":pago.serialize()},200
        return {"message":"Pago no encontrado"},404
        
    @classmethod
    def get_pago_by_pedido_id(cls, id_pedido):
        """Obtiene un pago por el ID del pedido asociado."""
        if id_pedido:
            pedido= Pedido.get_by_id(id_pedido)
            if pedido:
                pago= Pago.get_by_pedido_id(id_pedido)
                
                return jsonify({str(pedido["id_cliente"]):[pago,pedido]}),200
            return {"message":"Pago no encontrado porque el id del pedido no existe"}
        return {"message":"Pago no encontrado"},404
    
    @classmethod
    def get_all_pagos(cls):
        """Obtiene todos los pagos."""
        pagos= Pago.get_all()
        if pagos:
            return jsonify(pagos),200
        return {"message":"No hay pagos registrados"},404
    
    @classmethod
    def get_all(cls):
        """Obtiene todos los comprobantes."""
        comp= Comprobante.get_all()
        if comp:
            return jsonify(comp),200
        return {"message":"No hay comprobantes registrados"},404
    
    @classmethod
    def create_pago(cls):
        """Crea un nuevo pago. Se espera un JSON con id_pedido, metodo, monto, estado."""
        data=request.json
        if not data:
            return {"message":"Los campos no fueron completados"},400
        
        nuevo_pago= Pago(**data)
        pago_id= Pago.create(nuevo_pago)
        
        if pago_id:
            return {"message":"Pago creado exitosamente", "id_pago": pago_id},201
        return {"message":"Error al crear el pago"},500
    
    @classmethod
    def create_comprobante(cls):
        """se va a crear un comprobante cuando el estado del pago sea 'exitoso' 
        tiene que pasar el estado de pago pendiente, fallido o exitoso"""
        data=request.json
        if not data:
            return {"message":"Los campos no fueron completados"},400
        
        pago=Pago.get_by_id(data["id_pago"])
        id =Comprobante.create(Comprobante(id_pago=pago.id_pago))
        if id:
            return Comprobante.get_by_id(id_comprobante=id).serialize(),200
        return {"error": "No fue posible crear comprobante"}
    
    #metodos que solo puede utilizar el admin
    @classmethod
    def update_metodo_estado(cls):
        """Se podra actualizar el metodo o estado o ambos de un pago"""
        data=request.json
        pago=Pago(**data)
        if data and pago:
            Pago.update(pago)
            return {"message":"Pago actualizado correctamente"},200
        return {"messafe":"Error al actualizar pago"},400
    
    @classmethod
    def update_fecha_comprobante(cls):
        """puede actualizar su importe"""
        data=request.json
        if data:
            up_com=Comprobante(**data)
            Comprobante.update(up_com)
            return {"message":"fecha de comprobante "+str(up_com.id_comprobante)+" actualizado"},200
        return {"message":"Datos incompletos"}
    
    @classmethod
    def update_monto_pago(cls):
        """puede actualizar su importe """
        data=request.json
        if data:
            up_pago=Pago(**data)
            Pago.update_monto(up_pago)
            return {"message":"Monto de pago "+str(up_pago.id_pago)+" actualizado"},200
        return {"message":"Datos incompletos"}
    
    @classmethod
    def delete_pago(cls):
        data=request.json
        if data:
            Pago.delete(Pago(**data))
            return {"message":"Pago eliminado"},200
        return {"message":"Error al eliminar Pago"},400
    
    @classmethod
    def delete_comprobante(cls):
        data=request.json
        if data:
            Comprobante.delete(Comprobante(**data))
            return {"message":"Comprobante eliminado"},200
        return {"message":"Error al eliminar Comprobante"},400
    
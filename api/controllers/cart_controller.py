from ..models.carrito_model import Carrito
from ..models.carritoxitems_model import CarritoXItem
from flask import request, session, jsonify
class CartController:
    @classmethod
    def create_cart(cls):
        """SE CREA U CARRITO, pasar id_cliente"""
        data=request.json
        cart= Carrito(**data)
        id=Carrito.create(cart)
        if id:
            return {"message":"Carrito creado correctamente","id_carrito":id},200
        return {"error":"El carrito no pudo ser creado"},400
    
    #METODO UPDATE Y DELETE MANEJADOS POR UN ADMIN
    @classmethod
    def update_cart(cls):
        data=request.json
        if data:
            cart= Carrito(**data)
            if Carrito.update(cart):
                return {"message":"Carrito actualizado correctamente"},200
            return {"error":"No se pudo actualizar el carrito"},400
        return {"error":"No se pudo actualizar el carrito"},400
    
    @classmethod
    def delete_cart(cls):
        data=request.json
        if data:
            cart= Carrito(**data)
            Carrito.delete(cart)
            return {"message":"Carrito eliminado correctamente"},200
        return {"error":"No se pudo eliminar el carrito"},400
    
    @classmethod
    def get_all_carts(cls):
        carritos= Carrito.get_all()
        if carritos:
            return {"message":carritos},200
        return {"error":"No hay carritos para mostrar"},400
    
    @classmethod
    def get_cart(cls,id_cliente):
        cart= Carrito(id_cliente=id_cliente)
        carrito= Carrito.get_cart(cart)
        if carrito:
            items= CarritoXItem.get_items_by_cart(carrito)
            response=carrito.serialize()
            response['items']=items
            return {"message":response},200
        return {"error":"Carrito no encontrado, cliente no valido"},404
    
    @classmethod
    def add_item(cls):
        """agregar producto(item), pasar id_carrito,  id_producto, cantidad"""
        data=request.json
        carritoxitem= CarritoXItem(**data)
        if carritoxitem:
            id=CarritoXItem.add_item(carritoxitem)
            if id:
                return {"message":"Item agregado correctamente","id_cartxitem":id},200
            return {"error":"El item no pudo ser agregado"},400
        return {"message":"Datos incompletos"},400
    
    @classmethod
    def update_item(cls):
        """Actualizar cantidad"""
        data=request.json
        if data:
            carritoxitem= CarritoXItem(**data)
            CarritoXItem.update_item(carritoxitem)
            return {"message":"Item actualizado correctamente"},200
        return {"error":"No se pudo actualizar el item, datos incompletos"},400
    
    @classmethod
    def delete_item(cls):
        data=request.json
        if data:
            carritoxitem= CarritoXItem(**data)
            CarritoXItem.remove_item(carritoxitem)
            return {"message":"Item eliminado correctamente"},200
        return {"error":"No se pudo eliminar el item, datos incompletos"},400
    
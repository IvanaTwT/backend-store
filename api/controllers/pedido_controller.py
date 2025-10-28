from ..models.pedido_model import Pedido
from ..models.pedidoxitem_model import PedidoXItem
from ..models.carritoxitems_model import CarritoXItem
from ..models.domicilio_model import Domicilio
from ..models.product_model import Producto
from ..models.pago_model import Pago
from ..models.comprobante_model import Comprobante
from flask import request, session, jsonify
from ..controllers.users_controller import UserController
class PedidoController:
    @classmethod
    def create_pedido(cls):
        """Se crea un nuevo pedido"""
        data=request.json
        if data and "id_cliente" in data:
            #verificar que el cliente tenga un domicilio
            result= Domicilio.get(data.get("id_cliente"))
            if result:
                # print("DATA: ",data)
                pedido= Pedido(**data)
                # print("ES PDE: ",pedido.serialize())
                id=Pedido.create(pedido)
                if id:
                    return {"message":"Pedido creado correctamente","id_pedido":id},200
                return {"error":"El pedido no pudo ser creado"},400                
            return {"error":"Complete su domicilio"},400
        return {"error":"Hay campos sin completar"},400
    
    @classmethod
    def create_pedido_completo(cls):
        data = request.json

        if not data or "id_cliente" not in data or "items" not in data:
            return {"error": "Hay campos sin completar"}, 400

        id_cliente = data["id_cliente"]
        items = data["items"]
        domicilio_input = data.get("domicilio")
        data["estado"]="pendiente"
        data_pedido={"id_cliente":id_cliente, "estado":"pendiente","total":data["total"]}#object que tiene metodo, estado, monto(total)

        domicilio = Domicilio.get(id_cliente)
        if not domicilio:
            if not domicilio_input:
                return {"error": "El cliente no tiene domicilio registrado"}, 400
            
            # Crear domicilio nuevo
            nuevo_domicilio = Domicilio(
                id_cliente=id_cliente,
                domicilio=domicilio_input,
                ciudad="Salta Capital",
                codigo_postal="4400"
            )
            id_domicilio = Domicilio.create(nuevo_domicilio)
        else:
            id_domicilio = domicilio.id_domicilio
            # Si el usuario envió un domicilio distinto, podés actualizarlo:
            if domicilio_input and domicilio_input != domicilio.domicilio:
                domicilio.domicilio = domicilio_input
                Domicilio.update(domicilio)

        # Crear el pedido y los items (igual que antes)
        data_pedido["id_domicilio"] = id_domicilio
        pedido = Pedido(**data_pedido)
        id_pedido = Pedido.create(pedido)

        if not id_pedido:
            return {"error": "El pedido no pudo ser creado correctamente"}, 400

        creados = 0
        for item in items:            
            id_item = PedidoXItem.create(PedidoXItem(
                id_pedido=id_pedido,
                id_producto=item["id_producto"],
                cantidad=item["cantidad"],
                precioxunidad=item["precio"]
                ))            
            product= Producto.get(item["id_producto"])
            if id_item:            
                # eliminar item del carrito carritoxitem
                CarritoXItem.remove_item(CarritoXItem(id_carrito=data["id_carrito"], id_cartxitem=item["id_cartxitem"]))
                creados += 1
            
            #actualizar stock del producto
            if product.stock >= item["cantidad"]:
                product.stock = int(product.stock - item["cantidad"])
                Producto.update(product)
            else:
                return {"error": f"Stock insuficiente para el producto {product.id_producto}"}, 400
            
        if creados == len(items):
            if "estado" in data and "metodo" in data:
                data_pago={"id_pedido":id_pedido,"metodo":data["metodo"],"estado":data["estado"],"monto":data["total"]}
                new_pago= Pago.create(Pago(**data_pago))#devulve el id
                if new_pago:
                    id_comprobante= Comprobante.create(Comprobante(id_pago=new_pago))
                    if id_comprobante:
                        return {"message": "Pedido fue creado correctamente", "id_pedido": id_pedido, "id_pago":new_pago,"id_comprobante":id_comprobante}, 200
                    else:
                        return {"error":"Pedido y pago fueron creados con exito, en tanto al comprobante no se pudo realizar"}
                else:
                    return {"error": "EL metodo de pago no fue creado pero si pedido", "id_pedido": id_pedido}, 200
            else:
                return {"error": "Algunos valores no fueron agregados"}, 400
        return {"error": "Algunos items no pudieron ser creados"}, 400

    @classmethod
    def add_pedidoxitem(cls):
        """agregar pedido x item"""
        data=request.json
        if data:
            pedidoxitem= PedidoXItem(**data)
            id=PedidoXItem.create(pedidoxitem)
            if id:
                total=pedidoxitem.cantidad * pedidoxitem.precioxunidad
                Pedido.update_total(Pedido(id_pedido=pedidoxitem.id_pedido,total=total))
                return {"message":"Item agregado correctamente","id_pedidoxitem":id},200
            return {"error":"El item no pudo ser agregado"},400
        return {"message":"Datos incompletos"},400
    
    @classmethod
    def get_all_pedidos(cls):
        pedidos= Pedido.get_all()
        if pedidos:
            return {"message":pedidos},200
        return {"error":"No hay pedidos para mostrar"},400
    
    @classmethod
    def get_pedido(cls,id_cliente):
        """TRAER LOS DATOS DE UN PEDIDO POR EL ID_CLIENTE"""
        pedido= Pedido.get(id_cliente)
        if pedido:
            items= PedidoXItem.get_items_by_pedido(pedido)
            total_up=Pedido.get_by_id(pedido.id_pedido)
            response=total_up
            response['items']=items
            return {"message":response},200
        return {"error":"Pedido no encontrado"},404
    
    @classmethod
    def get_all_pedidos_more_items(cls,id_cliente):
        """TRAER TODOS LOS PEDIDOS DE UN CLIENTE"""
        pedidos= Pedido.get_all_pedidos(id_cliente)
        list_pedidos=[]
        if pedidos:
            for pedido in pedidos:
                items= PedidoXItem.get_items_by_pedido(pedido["id_pedido"])
                response=pedido
                response['items']=items
                list_pedidos.append(response)
            return {"message":list_pedidos},200
        return {"error":"No hay pedidos para mostrar"},404
    
    @classmethod
    def get_pedido_by_id(cls,id_pedido):
        """TRAER LOS DATOS DE UN PEDIDO"""
        pedido= Pedido.get_by_id(id_pedido)
        if pedido:
            items= PedidoXItem.get_items_by_pedido(pedido["id_pedido"])
            pedido["items"]=items
            return {"message":pedido},200
        return {"error":"Pedido no encontrado"},404
    
    #metodos de update, delete que puede manejar un ADMIN
    @classmethod
    def update_estado(cls):
        data=request.json
        user_data= UserController.verify_authentication()
        print("DAta",data)
        if data and "admin" in user_data:
            pedido= Pedido(**data)
            Pedido.update_estado(pedido)
            return {"message":"Estado del pedido actualizado correctamente"},200
        else:
            return {"error":"No se pudo actualizar el estado del pedido"},400
    
    @classmethod
    def update_total(cls):
        data=request.json
        user_data= UserController.verify_authentication()
        if "admin" in user_data and "total" in data and "id_pedido" in data:
            pedido= Pedido(**data)
            Pedido.update_total(pedido)
            return {"message":"Total del pedido actualizado correctamente"},200
        return {"error":"No se pudo actualizar el total del pedido"},400
    
    @classmethod
    def update_item(cls):
        data=request.json
        if data:
            item= PedidoXItem(**data)
            id_item=PedidoXItem.update_item(item)
            if id_item:
                data_item=PedidoXItem.get(id_item)
                total=data_item.cantidad * data_item.precioxunidad
                Pedido.update_total(Pedido(id_pedido=item.id_pedido,total=total))
                return {"message":"Item del pedido actualizado correctamente"},200
        return {"error":"No se pudo actualizar el item del pedido"},400
    
    @classmethod
    def delete_pedido(cls):
        data=request.json
        user_data= UserController.verify_authentication()
        if data and "admin" in user_data:
            pedido= Pedido(**data)
            Pedido.delete(pedido)
            return {"message":"Pedido eliminado correctamente"},200
        return {"error":"No se pudo eliminar el pedido"},400
    
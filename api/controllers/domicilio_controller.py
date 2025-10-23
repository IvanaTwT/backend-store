from ..models.domicilio_model import Domicilio
from flask import request, session, jsonify

class DomicilioController:
    @classmethod
    def create_domicilio(cls):
        data=request.json
        domi= Domicilio(**data)
        print("Domi: ",domi)
        id=Domicilio.create(domi)
        if id:
            return {"message":"Datos del domicilio cargados correctamente"},200
        return {"error":"Los datos del domicilio no pudieron ser cargados correctamente"},400
    
    @classmethod
    def get_domicilio(cls,id_domicilio):
        domi= Domicilio.get_domicilio(id_domicilio)
        if domi:
            return {"message":domi.serialize()},200
        return {"error":"Domicilio no encontrado"},404
    
    @classmethod
    def get_domicilio_by_idClient(cls,id_cliente):
        domi= Domicilio.get(id_cliente)
        if domi:
            return {"message":domi.serialize()},200
        return {"error":"Domicilio no encontrado"},404
    
    @classmethod
    def get_domicilio_client(cls,id_cliente):
        domi= Domicilio.get_all_domicilios(id_cliente)
        if isinstance(domi,list) :
            return {"message":domi},200
        elif domi :
            return{"message": domi.serialize()},200
        return {"error":"El cliente no ingreso los datos de su domicilio"},404
    
    @classmethod
    def update_address(cls):
        data=request.json
        if data:
            domi=Domicilio(**data)
            Domicilio.update(domi)
            return {"message":"Domicilio actualizado correctamente"},200
        return {"error":"No se pudo actualizar el domicilio"},400
    
    @classmethod
    def delete_address(cls,id_domicilio):
        domi=Domicilio(id_domicilio=id_domicilio)
        if domi:
            Domicilio.delete(domi)
            return {"message":"Domicilio eliminado correctamente"},200
        return {"error":"No se pudo eliminar el domicilio"},400            
        
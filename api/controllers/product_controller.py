from ..models.categoria_model import Categoria
from ..models.product_model import Producto
from flask import request, session, jsonify
from ..controllers.users_controller import UserController
class ProductController:
    #CRUD DE CATEGORIAS APROBED
    @classmethod
    def ver_categorias(cls):
        # print(str(session["user_id"])+"-"+str(session["admin"]))
        categorias=Categoria.get_categorias()
        if categorias:
            return {"message":categorias},200
        return {"error":"No hay categorias para mostrar"},
    
    @classmethod
    def ver_categoria(cls,id_categoria):
        categoria=Categoria.get(id_categoria)
        if categoria:
            return {"message":categoria.serialize()},200
        return {"error":"No hay categorias para mostrar"},400
    
    @classmethod
    def create_categoria(cls):
        data= request.json
        if data:
            categoria= Categoria(**data)
            new_id=Categoria.create(categoria)
            if new_id:
                return {"message":"Categoria '"+categoria.nombre+"' creada con exito"},200
            return {"message":"Error al crear categoria"},400
        return {"message":"No se insertaron datos"},400
    
    @classmethod
    def update_categoria(cls):
        try:
            data= request.json
            cate=Categoria(**data)
            response= Categoria.update(cate)
            if response:
                return {"message":"Los datos de categoria fueron actualizados correctamente"},200
            return {"error":"Esta categoria ya existe"},400
        except Exception as e:
            return {"error":"Error para actualizar"+str(e) },400
    @classmethod
    def delete_categoria(cls):
        try:
            data= request.json
            id=data["id_categoria"]
            cate=Categoria.get(id)
            nombre=cate["nombre"]
            # print(nombre)
            Categoria.delete(cate)
            return {"message":"Categoria: '"+nombre+"' eliminada"},200
        except Exception as e:
            return {"error":"Error para eliminar categoria"+str(e) },400
    #CRUD DE PRODUCT
    @classmethod
    def ver_producto(cls,id_producto):
        if (id_producto):
            producto=Producto.get(id_producto)
            if producto:
                return {"message":producto.serialize_with_categoria()},200
            return {"error":"Producto no encontrado"},404
        return {"error":"El id de producto no fue pasado"},400
    
    @classmethod
    def ver_productos(cls):
        productos=Producto.get_all()
        # print(productos)
        if productos:
            return {"message":productos},200
        return {"error":"No hay productos para mostrar"},404
    
    @classmethod
    def create_product(cls):
        data= request.json
        # print("Crear producto: ",data)
        user_data = UserController.verify_authentication()
        # print("DATA :",user_data)
        if user_data and "admin" in user_data:#es administrador
            if "id_categoria" in data and "user_id" in data:#si tiene el id
                producto= Producto(**data)
                # 'color': 'Rosa', 'precio': 28000, 'stock': 50, 'talle': 'S', 'categoria_edad': 'Niño'}
                new_id_product=Producto.create(producto)
                if new_id_product:
                    return {"message":"Producto #"+str(new_id_product)+" creado con exito", "id_producto":int(new_id_product)},200
            # else:
            #     categoria=Categoria(**data)
            #     new_id=Categoria.create(categoria)
            #     data["id_categoria"]=new_id
            #     producto= Producto(**data)
            #     new_id_product=Producto.create(producto)
            #     if new_id_product:
            #         return {"message":"Producto creado con exito"},200
            return {"message":"Error al crear producto"},400
        return {"error":"No tienes permisos para crear productos"},403
    
    @classmethod
    def update_product(cls):
        data=request.json
        print("Update product: ",data)
         # print("DATA :",user_data)
        user_data = UserController.verify_authentication()
        if user_data and "admin" in user_data: 
            categoria = data.get("id_categoria")
            # puede venir como dict (2ves) o número (1ves)
            if isinstance(categoria, dict):
                cate_id = categoria.get("id_categoria")
            else:
                cate_id = categoria

            data["id_categoria"] = cate_id
            
            prod = Producto(**data)
            print("product: ", prod.serialize())
            cate = Categoria(**{"id_categoria": cate_id})
            print("categoria: ", cate.serialize())
            product_old = Producto.get(prod.id_producto)
            print("product old: ", product_old)

            # misma categoría
            if product_old and product_old.id_categoria == cate.id_categoria:

                if isinstance(categoria, dict):
                    if categoria.get("nombre") or categoria.get("marca") or categoria.get("descripcion"):
                        Categoria.update(Categoria(**categoria))
                Producto.update(prod)
                return {"message": "Los datos del producto fueron actualizados correctamente"}, 200

            # cambiar categoría
            else:
                get_cate = Categoria.get(cate_id)
                if not get_cate:
                    return {"error": "La categoría no existe"}, 400
                            
                if isinstance(categoria, dict):
                    if categoria.get("nombre") or categoria.get("marca") or categoria.get("descripcion"):
                        Categoria.update(Categoria(**categoria))

                prod.id_categoria = cate_id
                Producto.update(prod)
                return {"message": "Los datos del producto fueron actualizados correctamente"}, 200
            
        return {"error": "No tienes permisos para crear productos"}, 403

    @classmethod
    def delete_product(cls):        
        try:
            data=request.json
            user_data = UserController.verify_authentication()
            # print("DATA :",user_data)
            if user_data and "admin" in user_data:#es administrador
                product=Producto(**data)
                Producto.delete(product)
                return {"message":"Producto eliminado"},200
            return {"error":"No tienes permisos para crear productos"},403
        except Exception as e:
            return {"error":"Error para actualizar"+str(e) },400
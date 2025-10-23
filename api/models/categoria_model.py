from ..database import DatabaseConnection

class Categoria:
    def __init__(self,**kwargs):
        self.id_categoria=kwargs.get("id_categoria")
        self.nombre=kwargs.get("nombre")
        self.marca=kwargs.get("marca","")
        self.descripcion=kwargs.get("descripcion","")
        
    def serialize(self):
        return {
            "id_categoria":self.id_categoria,
            "nombre":self.nombre,
            "marca":self.marca,
            "descripcion":self.descripcion
        }
    
    @classmethod
    def create(cls,categoria):
        """CREA CATEGORIA Y DEVUELVE SU ID"""
        if categoria and cls.exist_categoria(categoria.nombre) is False:
            sql="""INSERT INTO categoria(nombre,marca,descripcion) 
                    VALUES( %(nombre)s,%(marca)s,%(descripcion)s)"""
            
            cursor= DatabaseConnection.execute_query(query=sql,params=categoria.__dict__)
            
            if cursor:
                return cursor.lastrowid
        return None
    
    @classmethod
    def exist_categoria(cls,nombre):
        """VERIFICA SI EXISTE UNA CATEGORIA POR EL NOMBRE"""
        sql="SELECT*FROM categoria WHERE nombre=%s"
        result=DatabaseConnection.fetch_one(query=sql,params=(nombre,))
        
        if(result):
            return True
        return False
        
    @classmethod
    def get(cls,id_categoria):
        """TRAER DATOS DE UNA CATEGORIA POR EL ID PASADO"""
        sql="""SELECT*FROM categoria WHERE id_categoria=%s"""
        
        result=DatabaseConnection.fetch_one(query=sql,params=(id_categoria,))
        if result:
            return Categoria(
                    id_categoria=result[0],
                    nombre=result[1],
                    marca=result[2],
                    descripcion=result[3]
            )
        return None

    @classmethod
    def get_categorias(cls):
        """TRAER TODAS LAS CATEGORIAS"""
        sql="""SELECT*FROM categoria"""
        
        result=DatabaseConnection.fetch_all(query=sql)
        
        categorias=[]
        if result:
            for cate in result:
                categoria= Categoria(
                    id_categoria=cate[0],
                    nombre=cate[1],
                    marca=cate[2],
                    descripcion=cate[3]
                    ).serialize()
                categorias.append(categoria)
            return categorias
        return None
    
    @classmethod
    def update(cls, categoria):
        id=categoria.id_categoria
        categoria=categoria.__dict__
        # select*from categoria WHERE nombre="jeans" and id_categoria!=6;
        if cls.exist_categoria(categoria["nombre"]):
            #si ya existe una categoria con este nombre no deberia poder actualizar
            return False
          
        sql="UPDATE categoria SET "
        
        for clave,valor in categoria.items():
            if clave!="id_categoria" and valor:
                sql+=clave+"='"+str(valor)+"', "
            
        sql = sql.rstrip(", ")# # elimina la última coma y espacio
        sql+=" WHERE id_categoria = %s"
        print("mensaje SQL ",sql)
        DatabaseConnection.execute_query(query=sql,params=(id,))
        return True
    @classmethod
    def delete(cls,categoria):
        sql="""DELETE FROM categoria WHERE id_categoria= %(id_categoria)s"""
        DatabaseConnection.execute_query(query=sql,params=categoria)
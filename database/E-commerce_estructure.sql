create database ecommerce;
use  ecommerce;

create table usuario (
user_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
username VARCHAR(150) NOT NULL UNIQUE,
email VARCHAR(150) NOT NULL,
password VARCHAR(150) NOT NULL,
admin BOOLEAN NOT NULL DEFAULT 0,
inhabilitado BOOLEAN NOT NULL DEFAULT 0
);

-- Tabla token
CREATE TABLE tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(512) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expired_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuario(user_id) ON DELETE CASCADE
);

create table cliente(
	id_cliente INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    user_id INT NOT NULL,
	nombre_completo VARCHAR(200) NOT NULL,
	n_celular VARCHAR(10) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES usuario(user_id) ON DELETE CASCADE
);

create table domicilio(
	id_domicilio INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
    id_cliente INT NOT NULL,
    domicilio VARCHAR(500),
    ciudad VARCHAR(100) DEFAULT 'Salta Capital',
    codigo_postal VARCHAR(10) DEFAULT '4400',
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE
);

create table categoria(
	id_categoria INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    marca VARCHAR(150) NULL,
    descripcion  VARCHAR(100) NULL
    );
create table producto(
	id_producto INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    user_id INT NOT NULL,
    id_categoria INT NOT NULL,
    path_image VARCHAR(900) NOT NULL,
    color ENUM('Blanco','Beige','Negro','Azul Marino','Celeste','Rosa') NOT NULL,
    precio FLOAT NOT NULL,
    stock INT NOT NULL, 
    talle ENUM('XXS','XS','S','M','L','XL','XXL','4','6','8','10','36','38','40','42','44','46','48','50') NOT NULL,
    categoria_edad ENUM('Niño','Mujer','Hombre') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usuario(user_id) ON DELETE CASCADE,
	FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria) 
    ON UPDATE CASCADE
    ON DELETE CASCADE  
    );
    
create table carrito(
	id_carrito INT AUTO_INCREMENT KEY UNIQUE NOT NULL,
    id_cliente INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE
    );
    
create table carritoXitem(
	id_cartxitem INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL,
    id_carrito INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_carrito) REFERENCES carrito(id_carrito) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto) ON DELETE CASCADE
    );
    
create table pedido(
	id_pedido INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
    id_cliente INT NOT NULL,
    id_domicilio INT NOT NULL,    
    total FLOAT NOT NULL,
    estado ENUM('pendiente','pagado','cancelado')  NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY(id_domicilio) REFERENCES domicilio(id_domicilio) ON DELETE CASCADE
);

create table pedidoXitem(
	id_pedidoxitem INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
	cantidad INT NOT NULL,
    precioxunidad FLOAT NOT NULL ,
	FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto) ON DELETE CASCADE
);
  -- DEFAULT 0.00  
create table pago(
	id_pago  INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
    id_pedido INT NOT NULL,
    metodo ENUM('mercado pago','efectivo','50-50'),
    monto FLOAT NOT NULL,
    estado ENUM('pendiente','exitoso','fallido'),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE
);

create table comprobante(
	id_comprobante INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
    id_pago INT NOT NULL,
    n_comprobante VARCHAR(300) NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(id_pago) REFERENCES pago(id_pago) ON DELETE CASCADE
);    

create table valoracion(
	id_valoracion INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
	id_cliente INT NOT NULL,
    id_producto INT NOT NULL,
    calificacion ENUM('Malo','Regular','Bueno','Muy Bueno','Excelente') NOT NULL,
    estrellas INT NOT NULL,
    comentario VARCHAR(2500) NULL,
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto) ON DELETE CASCADE
);
use ecommerce;
INSERT INTO usuario(username,email,password, admin)
VALUES
('admin1','maria@gmail.com','25f43b1486ad95a1398e3eeb3d83bc4010015fcc9bedb35b432e00298d5021f7',1),
('admin2','terry@gmail.com','1c142b2d01aa34e9a36bde480645a57fd69e14155dacfab5a3f9257b77fdc8d8',1),
('admin3','gilbert@gmail.com','4fc2b5673a201ad9b1fc03dcb346e1baad44351daa0503d5534b4dfdcc4332e0',1),
('Jaz','jazmin@gmail.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',0),
('Dami','damian@gmail.com','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',0)
;
INSERT INTO cliente(user_id, nombre_completo, n_celular)
VALUES
(4,'Jazmin Morales','387465435'),
(5,'Damian Robles','3871568922')
;

INSERT INTO categoria(nombre)
values
('Remera'),
('Camiseta'),
('Musculosa'),
('Campera'),
('Buzo'),
('Jeans'),
('Jeans cargo'),
('Medias')
;

INSERT INTO producto(user_id, id_categoria, color, path_image,precio, stock, talle, categoria_edad)
VALUES
(1,1,'Negro','https://i.pinimg.com/1200x/a1/7c/4d/a17c4d6e0af41cfdb359f3ef8e6c6bdb.jpg',5500,100,'S','Mujer'),
(1,1,'Azul Marino','https://i.pinimg.com/1200x/34/68/56/3468565bee0db9e6aefa02907b235fe7.jpg',5500,100,'S','Mujer'),
(1,1,'Blanco','https://i.pinimg.com/736x/c0/3b/e2/c03be2f3900c3c611ded998c241a3a78.jpg',5500,100,'S','Mujer'),
(1,1,'Celeste','https://i.pinimg.com/1200x/ad/74/42/ad74425f16df9f762359bfcbd6fa799b.jpg',5500,100,'S','Mujer'),
(1,1,'Negro','https://i.pinimg.com/736x/7f/02/6d/7f026dc5acb8cc87c3cec740678615cd.jpg',6000,100,'M','Mujer'),
(1,1,'Azul Marino','https://i.pinimg.com/1200x/bf/3e/c6/bf3ec6d32f48572f31c301f2632864b2.jpg',6000,100,'M','Mujer'),
(1,1,'Blanco','https://i.pinimg.com/1200x/b6/35/1d/b6351d9d05e7124c4c65c8a177194a1e.jpg',6000,100,'M','Mujer'),
(1,1,'Celeste','https://i.pinimg.com/736x/19/27/1a/19271a1fe0916e10e144c67e70fe18b4.jpg',6000,100,'M','Mujer'),
(1,1,'Negro','https://i.pinimg.com/1200x/67/6c/af/676cafdca5acdf8e9a86716178920c7c.jpg',6500,100,'L','Mujer'),
(1,1,'Azul Marino','https://i.pinimg.com/1200x/5b/7a/2e/5b7a2ee84243b36c3edc42d29db508ba.jpg',6500,100,'L','Mujer'),
(1,1,'Blanco','https://i.pinimg.com/1200x/dc/bc/38/dcbc385879c447f107f171e5a351c525.jpg',6500,100,'L','Mujer'),
(1,1,'Celeste','https://i.pinimg.com/736x/4e/07/c4/4e07c4fb495234db02c0658ce724c668.jpg',6500,100,'L','Mujer'),
(1,1,'Negro','https://i.pinimg.com/1200x/5e/a0/df/5ea0df0025eeed5e6ae7dd9124a4ffac.jpg',7500,100,'S','Hombre'),
(1,1,'Azul Marino','https://i.pinimg.com/1200x/6c/e4/dd/6ce4dd57d45614521577f50851127412.jpg',7500,100,'S','Hombre'),
(1,1,'Blanco','https://i.pinimg.com/1200x/15/f4/71/15f471d3a4254d7b615fb3e1eeaf9ca9.jpg',7500,100,'S','Hombre'),
(1,1,'Celeste','https://i.pinimg.com/736x/ab/9e/1e/ab9e1ed2ef5fa33ece7795661e3e9e5b.jpg',7500,100,'S','Hombre'),
(1,1,'Negro','https://i.pinimg.com/736x/e8/9d/63/e89d63b118bf723c5ce4b81e9e6ab621.jpg',8000,100,'M','Hombre'),
(1,1,'Azul Marino','https://i.pinimg.com/1200x/0c/de/e6/0cdee6f532effdbd90bf40f5d6099594.jpg',8000,100,'M','Hombre'),
(1,1,'Blanco','https://i.pinimg.com/736x/5c/eb/f2/5cebf29f5b5f90ab6923d37f5d78c0f2.jpg',8000,100,'M','Hombre'),
(1,1,'Celeste','https://i.pinimg.com/1200x/d5/4f/ae/d54fae9b33a1dffe77b7b9fc85c482e0.jpg',8000,100,'M','Hombre'),
(1,1,'Negro','https://i.pinimg.com/1200x/4c/a5/3b/4ca53b0e8eb45a2b51aa07d5fe24dd70.jpg',8500,100,'L','Hombre'),
(1,1,'Azul Marino','https://i.pinimg.com/1200x/71/8e/e9/718ee9fc152f5612f0f656cfacc99c9a.jpg',8500,100,'L','Hombre'),
(1,1,'Blanco','https://i.pinimg.com/1200x/d5/98/c8/d598c8df6b163dbd1d00a45783ec9d29.jpg',8500,100,'L','Hombre'),
(1,1,'Celeste','https://i.pinimg.com/1200x/5e/08/40/5e0840cb75a955148740bfef5049b152.jpg',8500,100,'L','Hombre'),
(2,1,'Negro','https://i.pinimg.com/736x/7c/ba/61/7cba6161a495856b1eadab794e667161.jpg',4000,100,'XXS','Niño'),
(2,1,'Azul Marino','https://i.pinimg.com/736x/89/45/ba/8945ba1600d2ffeafb97d73c07b05fd8.jpg',4000,100,'XXS','Niño'),
(2,1,'Blanco','https://i.pinimg.com/1200x/ce/0f/32/ce0f32758b268fff638ef89cdc54a6e6.jpg',4000,100,'XXS','Niño'),
(2,1,'Negro','https://i.pinimg.com/736x/c8/36/43/c8364344a7d6e04927037bca43adafbf.jpg',4500,100,'XS','Niño'),
(2,1,'Azul Marino','https://i.pinimg.com/1200x/d2/36/e0/d236e0c20e8f84d9b77988d2e2e8186d.jpg',4500,100,'XS','Niño'),
(2,1,'Blanco','https://i.pinimg.com/736x/5d/b1/68/5db168bf15c565f8928fe1b1f2a156b8.jpg',4500,100,'XS','Niño'),
(2,1,'Negro','https://i.pinimg.com/1200x/fb/d2/40/fbd240e799f81947dcbf1d57ea305bc6.jpg',5000,100,'S','Niño'),
(2,1,'Azul Marino','https://i.pinimg.com/736x/78/73/7f/78737f0b76023f0f946e5a15a6c1213d.jpg',5000,100,'S','Niño'),
(2,1,'Blanco','https://i.pinimg.com/736x/e2/f4/e0/e2f4e08bae5c16e9da4573b0daa1ec6f.jpg',5000,100,'S','Niño'),
(3,2,'Negro','https://i.pinimg.com/1200x/16/2f/48/162f485ee2992b7e6f6a7fa1872c8671.jpg',6000,100,'XXS','Niño'),
(3,2,'Negro','https://i.pinimg.com/1200x/ad/1a/df/ad1adfcc45ebef5a63ca2bfa84e9a536.jpg',6500,100,'XS','Niño'),
(3,2,'Negro','https://i.pinimg.com/1200x/66/95/b2/6695b22b4a03de09f80b9e31114b0e95.jpg',7000,100,'S','Niño'),
(3,2,'Blanco','https://i.pinimg.com/1200x/32/20/1e/32201eb39f537e67b8f50102ebd03fe9.jpg',6000,100,'XXS','Niño'),
(3,2,'Blanco','https://i.pinimg.com/1200x/fe/4f/c7/fe4fc7080c90853a991d28e3c88aff9e.jpg',6500,100,'XS','Niño'),
(3,2,'Blanco','https://i.pinimg.com/736x/3d/08/1b/3d081bdd68914f737eaae8cbe364b0dc.jpg',7000,100,'S','Niño'),
(3,2,'Negro','https://i.pinimg.com/1200x/dd/ac/65/ddac65a269cd08769090c1952454d685.jpg',7500,100,'S','Mujer'),
(3,2,'Blanco','https://i.pinimg.com/736x/04/67/73/04677369ec7fc4bc5e5fef3856eeeee5.jpg',7500,100,'S','Mujer'),
(3,2,'Negro','https://i.pinimg.com/1200x/36/08/3d/36083d915b508018305e5632b1a821ef.jpg',8000,100,'M','Mujer'),
(3,2,'Blanco','https://i.pinimg.com/1200x/44/d3/ef/44d3ef4a0474ea3a336572c073f2dba2.jpg',8000,100,'M','Mujer'),
(3,2,'Negro','https://i.pinimg.com/736x/c1/89/3e/c1893e1c04d4d247bd5425c795e28065.jpg',8500,100,'L','Mujer'),
(3,2,'Blanco','https://i.pinimg.com/1200x/1a/21/15/1a2115d6e2824bd8f7f70ab753764e7d.jpg',8500,100,'L','Mujer'),
(3,2,'Negro','https://i.pinimg.com/1200x/74/7f/70/747f70d5a260ddb6eb26f590c048ac5a.jpg',9000,100,'S','Hombre'),
(3,2,'Blanco','https://i.pinimg.com/1200x/7a/e1/be/7ae1be2f68b4021a5a791e0d08c71f0a.jpg',9000,100,'S','Hombre'),
(3,2,'Negro','https://i.pinimg.com/1200x/80/d0/74/80d07419d76470fe16b11a91abd9650c.jpg',9500,100,'M','Hombre'),
(3,2,'Blanco','https://i.pinimg.com/736x/c7/c3/fe/c7c3fea916ce1a6c95755ca630bea326.jpg',9500,100,'M','Hombre'),
(3,2,'Negro','https://i.pinimg.com/736x/ad/01/3b/ad013b9ff3acc8cea0c52ff2c62d3ba2.jpg',10000,100,'L','Hombre'),
(3,2,'Blanco','https://i.pinimg.com/736x/cb/db/f6/cbdbf631e0f8869d51645cb99e85bde2.jpg',10000,100,'L','Hombre'),
(3,7,'Celeste','https://i.pinimg.com/736x/aa/5f/8d/aa5f8de7ef03cd2aec4e0cf0d44fd501.jpg',24500,100,'38','Mujer'),
(3,7,'Celeste','https://i.pinimg.com/1200x/2b/70/57/2b70575ca983e991995abb19a77ca17f.jpg',28500,100,'40','Mujer'),
(3,7,'Celeste','https://i.pinimg.com/736x/01/91/3d/01913dfcf9128e671c3036f8e18dd964.jpg',32500,100,'42','Mujer'),
(3,7,'Celeste','https://i.pinimg.com/736x/de/c0/78/dec078eb681f7e78d0d3ea5e66a4383c.jpg',35000,100,'40','Hombre'),
(3,7,'Celeste','https://i.pinimg.com/1200x/ba/8d/0d/ba8d0d5dadca2d41f88475e603e22454.jpg',40000,100,'44','Hombre'),
(3,7,'Celeste','https://i.pinimg.com/1200x/6f/a2/9a/6fa29a47a6502eec5b170ec627cd7894.jpg',45000,100,'48','Hombre'),
(3,7,'Celeste','https://i.pinimg.com/1200x/bd/e0/16/bde016497532d2c47b9fc89b1490c8dc.jpg',18500,100,'4','Niño'),
(3,7,'Celeste','https://i.pinimg.com/1200x/65/d7/77/65d77752c3e7fd32853dd6bbd4129b32.jpg',205000,100,'8','Niño'),
(3,7,'Celeste','https://i.pinimg.com/1200x/77/9a/a7/779aa7fbd998fd9d6da93d56bc09aad1.jpg',22500,100,'10','Niño');

INSERT INTO domicilio(id_cliente, domicilio)
VALUES (1, 'Av. Siempre Viva 742');

INSERT INTO carrito(id_cliente) VALUES (1);

INSERT INTO carritoxitem(id_carrito, id_producto, cantidad)
VALUES 
(1, 1, 2),
(1, 2, 1);

INSERT INTO pedido(id_cliente, id_domicilio , total, estado)
VALUES (1, 1, 16500, 'pendiente');

INSERT INTO pedidoxitem(id_pedido, id_producto, cantidad, precioxunidad)
VALUES
(1, 1, 2, 5500),
(1, 2, 1, 5500);

INSERT INTO pago(id_pedido, metodo, monto, estado)
VALUES (1, 'mercado pago', 16500, 'pendiente');

INSERT INTO comprobante(id_pago, n_comprobante)
VALUES (1, 'A-0000-000001');

INSERT INTO valoracion(id_cliente,id_producto,calificacion,estrellas,comentario)
VALUES(1,1,'Muy Bueno',4,'Muy buena calidad y diseño');
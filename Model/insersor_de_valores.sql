INSERT INTO USUARIOS (login, senha, cargo)
	VALUES
		('Usuario01', 'Senha001' ,'Estoquista'),
		('Usuario02', 'Senha002' ,'Administrador'),
		('Usuario03', 'senha003' ,'Estoquista');

INSERT INTO FORNECEDORES (cnpj,nome_fornecedor,endereco,email,telefone)
	VALUES 
		('12345678912345', 'Fornecedor001','rua da lua', 'Fornecedor001@gmail.com','11997841234'),
		('09876543211234', 'Fornecedor002','rua do sol', 'Fornecedor002@gmail.com','11912345678'),
		('09877867723466', 'Fornecedor003','rua de marte', 'Fornecedor003@gmail.com','11989764532');

INSERT INTO PEDIDOS (data_pedido)  
	VALUES 
    	('2024-03-17 14:30:00'),
    	('2024-03-16 09:15:00'),
    	(DEFAULT);

INSERT INTO PRODUTOS (cod_produto, nome_produto, quantidade, preco_unitario, categoria, descricao) 
	VALUES 
    	(9800, 'Teclado Mecânico', 50, 249.99, 'Periféricos', 'Teclado RGB com switches mecânicos'),
    	(8700, 'Monitor Full HD', 20, 799.00, 'Monitores', 'Monitor de 24 polegadas com painel IPS'),
    	(7600, 'Cadeira Gamer', 15, 1199.99, 'Móveis', 'Cadeira ergonômica com ajuste de altura');

INSERT INTO FORNECE (id_pedido,cnpj_fornecedor,cod_produto,quantidade)
	VALUES 
		(1, '09877867723466', 9800, 50),
		(2, '12345678912345', 8700, 20),
		(3, '09876543211234', 7600, 15);

INSERT INTO MOVIMENTA (evento,quantidade,cod_produto,usuario)
	VALUES
		('Entrada', 50, 9800, 'Usuario01'),
		('Entrada', 20, 8700, 'Usuario01'),
		('Entrada', 15, 7600, 'Usuario03');
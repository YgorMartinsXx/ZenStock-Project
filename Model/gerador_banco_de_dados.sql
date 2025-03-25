
create table USUARIOS (
	login VARCHAR(17) primary key,
	senha VARCHAR(20) not null,
	cargo VARCHAR(15) not null CHECK(cargo in('Estoquista', 'Administrador'))
);

create table PRODUTOS (
	cod_produto  	INT 		 primary key,
	nome_produto 	VARCHAR(30)  not null,
	quantidade	 	INT 		 not null,
	preco_unitario	DECIMAL(7,2) not null,
	categoria		VARCHAR(40)  not null,
	descricao		VARCHAR(50)
);

create table FORNECEDORES (
	cnpj 			CHAR(14) 	primary key,
	nome_fornecedor VARCHAR(40) not null,
	endereco 		VARCHAR(40) not null,
	email			VARCHAR(40) not null,
	telefone		CHAR(11)	not null
);

create table PEDIDOS (
	id_pedido	INT primary key auto_increment,
	data_pedido DATETIME not null default CURRENT_TIMESTAMP
);

create table FORNECE(
	id_pedido 		INT,
	cnpj_fornecedor CHAR(14),
	cod_produto 	INT,
	quantidade 		INT,
	
	constraint fkFornece_Produto 	 FOREIGN KEY(cod_produto)	  references PRODUTOS(cod_produto)
     	on delete cascade
     	on update cascade,
     	
     constraint fkFornecedor_Fornece FOREIGN KEY(cnpj_fornecedor) references FORNECEDORES(cnpj)
     	on delete cascade
     	on update cascade,
     	
     constraint fkPedido_Fornecido 	 FOREIGN KEY(id_pedido)		  references PEDIDOS(id_pedido)
     	on delete cascade
     	on update cascade
);


create table MOVIMENTA (
    id_movimentacao 	INT  	    primary key auto_increment,
    evento          	VARCHAR(7)  not null CHECK(evento IN ('Entrada', 'Saida')),
    quantidade 			INT		  	not null,
    data_movimentacao	DATETIME 	not null default CURRENT_TIMESTAMP,
    cod_produto			INT,
    usuario				VARCHAR(17),
    
     constraint fkMovimenta_Produto  FOREIGN KEY(cod_produto) references PRODUTOS(cod_produto)
     	on delete cascade
     	on update cascade,
     	
     constraint fkUsuario_Movimenta  FOREIGN KEY(usuario)	  references USUARIOS(login)
     	on delete cascade
     	on update cascade
);

from database_connection import Session

from Model.classe_pedido import Pedidos
from Model.classe_fornecedores import Fornecedores
from Model.classe_fornece import Fornece
from Model.classe_produtos import Produto
from Model.classe_movimenta import Movimenta
from Model.classe_usuarios import Usuarios

def criar_pedido(cnpj_fornecedor,cod_produto, quantidade_fornecida, login_usuario):
    session = Session()
    try:
        # Buscar o CNPJ do fornecedor
        fornecedor = session.query(Fornecedores).filter_by(cnpj=cnpj_fornecedor).first()
        if not fornecedor:
            return {"erro": "Fornecedor não encontrado"}, 404

        # Buscar o codigo do produto
        produto = session.query(Produto).filter_by(cod_produto=cod_produto).first()
        if not produto:
            return {"erro": "produto não encontrado"}, 404
        
        # Criar um novo pedido
        novo_pedido = Pedidos()
        session.add(novo_pedido)
        session.commit()  # Commit para gerar o ID do pedido

        # Criar a relação na tabela FORNECE
        novo_fornece = Fornece(id_Pedido=novo_pedido.id_Pedido, cnpj_fornecedor=cnpj_fornecedor, cod_produto = int(cod_produto), quantidade = int(quantidade_fornecida) )
        session.add(novo_fornece)
        session.commit()

        # conclusão do ciclo. Criando a relação na entidade Movimenta
        # Buscar o login do usuario
        usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
        if not usuario:
            return {"erro": "Usuario não encontrado"}, 404
        
        novo_movimenta = Movimenta(evento = 'Entrada', quantidade = int(quantidade_fornecida), cod_produto = int(cod_produto), usuario = login_usuario  )
        session.add(novo_movimenta)
        session.commit()

        return {
            "mensagem": "Pedido criado e relacionado ao fornecedor e ao pedido com sucesso!",
            "id_Pedido": novo_pedido.id_Pedido,
            "cnpj_fornecedor": fornecedor.cnpj,
            "cod_produto": produto.cod_produto,
            "usuario": usuario.login
        }, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 500
    
    finally:
        session.close()


def excluir_pedido(id_pesquisado):
    session = Session()

    try:
        # Buscar o id do pedido
        pedido = session.query(Produto).filter_by(id_Pedido = int(id_pesquisado)).first()
        if not pedido:
            return {"erro": "pedido não encontrado"}, 404
        
         # Remover primeiro a relação na tabela FORNECE
        session.query(Fornece).filter_by(id_pedido = int(id_pesquisado)).delete()

         # Remover o pedido da tabela PEDIDOS
        session.delete(pedido)
        session.commit()

    except:
        session.rollback()
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()


def buscar_pedido(id_pedido):
    session = Session()

    try:
        # Buscar o id do pedido
        pedido = session.query(Produto).filter_by(id_Pedido = int(id_pedido)).first()
        if not pedido:
            return {"erro": "pedido não encontrado"}, 404
        
        pedidos_json = [
            {"id_Pedido": pedido.id_Pedido, "data_Pedido": pedido.data_Pedido}
            ]

        return pedidos_json,200

    except Exception as e:
        return {"erro": str(e)}, 500
    
    finally:
        session.close()


def todos_pedidos():
    session = Session()
    try:
        # Buscar todos os pedidos
        pedidos = session.query(Pedidos).all()
        
        if not pedidos:
            return {"erro": "Nenhum pedido encontrado"}, 404

        # Converter os pedidos para um formato JSON
        pedidos_json = [
            {"id_Pedido": pedido.id_Pedido, "data_Pedido": pedido.data_Pedido}
            for pedido in pedidos
        ]

        return pedidos_json, 200

    except:
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()
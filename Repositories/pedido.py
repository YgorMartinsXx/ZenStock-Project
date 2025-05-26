from database_connection import Session

from Model.classe_pedido import Pedidos
from Model.classe_fornecedores import Fornecedores
from Model.classe_fornece import Fornece
from Model.classe_produtos import Produto
from Model.classe_movimenta import Movimenta
from Model.classe_usuarios import Usuarios

class GerenciadorPedidos:

    @staticmethod
    def criar_pedido(cnpj_fornecedor, cod_produto, quantidade_fornecida, login_usuario):
        session = Session()
        try:
            # Buscar o fornecedor
            fornecedor = session.query(Fornecedores).filter_by(cnpj=cnpj_fornecedor).first()
            if not fornecedor:
                return {"erro": "Fornecedor não encontrado."}, 404

            # Buscar o produto
            produto = session.query(Produto).filter_by(cod_produto=cod_produto).first()
            if not produto:
                return {"erro": "Produto não encontrado."}, 404
            
            # Criar um novo pedido
            novo_pedido = Pedidos()
            session.add(novo_pedido)
            session.commit()

            # Criar a relação na tabela FORNECE
            novo_fornece = Fornece(
                id_pedido=novo_pedido.id_Pedido, 
                cnpj_fornecedor=cnpj_fornecedor, 
                cod_produto=int(cod_produto), 
                quantidade=int(quantidade_fornecida)
            )
            session.add(novo_fornece)
            session.commit()

            # Buscar o usuário
            usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
            if not usuario:
                return {"erro": "Usuário não encontrado."}, 404
            
            # Registrar movimentação
            novo_movimenta = Movimenta(
                evento='Entrada', 
                quantidade=int(quantidade_fornecida), 
                cod_produto=int(cod_produto), 
                usuario=login_usuario
            )
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
            return {"erro": f"Erro inesperado: {str(e)}"}, 500
        
        finally:
            session.close()


    @staticmethod
    def excluir_pedido(id_pesquisado):
        session = Session()

        try:
            pedido = session.query(Pedidos).filter_by(id_Pedido=int(id_pesquisado)).first()

            if not pedido:
                return {"erro": "Pedido não encontrado."}, 404

            session.query(Fornece).filter_by(id_pedido=int(id_pesquisado)).delete()
            session.delete(pedido)
            session.commit()

            return {"mensagem": "Pedido excluído com sucesso."}, 200

        except Exception as e:
            session.rollback()
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()


    @staticmethod
    def buscar_pedido(id_pedido):
        session = Session()

        try:
            pedido = session.query(Pedidos).filter_by(id_Pedido=int(id_pedido)).first()

            if not pedido:
                return {"erro": "Pedido não encontrado."}, 404

            pedidos_json = {
                "id_Pedido": pedido.id_Pedido,
                "data_Pedido": pedido.data_Pedido
            }

            return pedidos_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()


    @staticmethod
    def todos_pedidos():
        session = Session()
        try:
            pedidos = session.query(Pedidos).all()
            
            if not pedidos:
                return {"erro": "Nenhum pedido encontrado"}, 404

            pedidos_json = [
                {"id_Pedido": pedido.id_Pedido, "data_Pedido": pedido.data_Pedido}
                for pedido in pedidos
            ]

            return pedidos_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500
        
        finally:
            session.close()

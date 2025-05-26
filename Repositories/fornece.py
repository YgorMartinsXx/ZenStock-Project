from database_connection import Session
from Model.classe_produtos import Produto
from Model.classe_fornecedores import Fornecedores
from Model.classe_fornece import Fornece


class GerenciadorFornecimentos:
    """
    Esta classe encapsula as operações relacionadas à entidade 'Fornece',
    permitindo buscar, listar, editar e deletar registros de fornecimento.
    Todas as interações com o banco de dados são gerenciadas de forma segura
    com controle de exceções e fechamento da sessão.
    """

    @staticmethod
    def buscar_fornecimento(id_pesquisado: int):
        """
        Busca um fornecimento específico pelo ID do pedido.
        """
        session = Session()

        try:
            fornecimento = session.query(Fornece).filter_by(id_pedido=int(id_pesquisado)).first()

            if not fornecimento:
                return {"erro": "Fornecimento não encontrado."}, 404

            fornecimento_json = {
                "id_Pedido": fornecimento.id_pedido,
                "cnpj_fornecedor": fornecimento.cnpj_fornecedor,
                "cod_produto": fornecimento.cod_produto,
                "quantidade": fornecimento.quantidade
            }

            return fornecimento_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def todos_fornecimentos():
        """
        Retorna uma lista com todos os fornecimentos cadastrados.
        """
        session = Session()

        try:
            fornecimentos = session.query(Fornece).all()

            if not fornecimentos:
                return {"erro": "Nenhum fornecimento encontrado."}, 404

            fornecimento_json = [
                {
                    "id_Pedido": fornecimento.id_pedido,
                    "cnpj_fornecedor": fornecimento.cnpj_fornecedor,
                    "cod_produto": fornecimento.cod_produto,
                    "quantidade": fornecimento.quantidade,
                }
                for fornecimento in fornecimentos
            ]

            return fornecimento_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def fornecimento_por_produto(codigo_produto):
        """
        Retorna todos os fornecimentos associados a um determinado código de produto.
        """
        session = Session()

        try:
            fornecimentos = session.query(Fornece).filter_by(cod_produto=int(codigo_produto)).all()

            if not fornecimentos:
                return {"erro": "Nenhum fornecimento encontrado para este produto."}, 404

            fornecimento_json = [
                {
                    "id_Pedido": fornecimento.id_pedido,
                    "cnpj_fornecedor": fornecimento.cnpj_fornecedor,
                    "cod_produto": fornecimento.cod_produto,
                    "quantidade": fornecimento.quantidade,
                }
                for fornecimento in fornecimentos
            ]

            return fornecimento_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def fornecimento_por_fornecedor(cnpj_fornecedor):
        """
        Retorna todos os fornecimentos associados a um determinado fornecedor.
        """
        session = Session()

        try:
            fornecimentos = session.query(Fornece).filter_by(cnpj_fornecedor=cnpj_fornecedor).all()

            if not fornecimentos:
                return {"erro": "Nenhum fornecimento encontrado para este fornecedor."}, 404

            fornecimento_json = [
                {
                    "id_Pedido": fornecimento.id_pedido,
                    "cnpj_fornecedor": fornecimento.cnpj_fornecedor,
                    "cod_produto": fornecimento.cod_produto,
                    "quantidade": fornecimento.quantidade,
                }
                for fornecimento in fornecimentos
            ]

            return fornecimento_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def deleta_fornecimento(id_pesquisado):
        """
        Deleta um fornecimento com base no ID do pedido.
        """
        session = Session()

        try:
            pedido = session.query(Fornece).filter_by(id_pedido=int(id_pesquisado)).first()

            if not pedido:
                return {"erro": "Fornecimento não encontrado."}, 404

            session.delete(pedido)
            session.commit()

            return {"mensagem": "Fornecimento excluído com sucesso."}, 200

        except Exception as e:
            session.rollback()
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def editar_fornecimento(id_pedido=None, novo_cnpj=None, novo_cod_produto=None, nova_quantidade=None):
        """
        Edita os dados de um fornecimento com base no ID do pedido.
        Pode atualizar o CNPJ do fornecedor, o código do produto e a quantidade.
        """
        session = Session()

        try:
            fornecimento = session.query(Fornece).filter_by(id_pedido=int(id_pedido)).first()

            if not fornecimento:
                return {"erro": "Fornecimento não encontrado."}, 404

            if novo_cnpj is not None:
                fornecedor_existe = session.query(Fornecedores).filter_by(cnpj=novo_cnpj).first()
                if not fornecedor_existe:
                    return {"erro": "Fornecedor não encontrado."}, 400

            if novo_cod_produto is not None:
                produto_existe = session.query(Produto).filter_by(cod_produto=int(novo_cod_produto)).first()
                if not produto_existe:
                    return {"erro": "Produto não encontrado."}, 400

            if novo_cnpj is not None:
                fornecimento.cnpj_fornecedor = novo_cnpj

            if novo_cod_produto is not None:
                fornecimento.cod_produto = int(novo_cod_produto)

            if nova_quantidade is not None:
                fornecimento.quantidade = int(nova_quantidade)

            session.commit()
            return {"mensagem": "Fornecimento atualizado com sucesso."}, 200

        except Exception as e:
            session.rollback()
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

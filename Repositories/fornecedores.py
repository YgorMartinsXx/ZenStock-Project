from database_connection import Session
from Model.classe_fornecedores import Fornecedores


class GerenciadorFornecedores:
    """
    Classe responsável pelas operações relacionadas à entidade 'Fornecedores'.
    Inclui funcionalidades de criação, leitura, atualização e exclusão.
    """

    @staticmethod
    def buscar_fornecedor(cnpj_pesquisado):
        session = Session()
        try:
            fornecedor = session.query(Fornecedores).filter_by(cnpj=cnpj_pesquisado).first()

            if not fornecedor:
                return {"erro": "Fornecedor não encontrado."}, 404

            fornecedor_json = {
                "cnpj": fornecedor.cnpj,
                "nome_fornecedor": fornecedor.nome_fornecedor,
                "endereco": fornecedor.endereco,
                "email": fornecedor.email,
                "telefone": fornecedor.telefone
            }

            return fornecedor_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def todos_fornecedores():
        session = Session()
        try:
            fornecedores = session.query(Fornecedores).all()

            if not fornecedores:
                return {"erro": "Nenhum fornecedor encontrado."}, 404

            fornecedores_json = [
                {
                    "cnpj": f.cnpj,
                    "nome_fornecedor": f.nome_fornecedor,
                    "endereco": f.endereco,
                    "email": f.email,
                    "telefone": f.telefone
                }
                for f in fornecedores
            ]

            return fornecedores_json, 200

        except Exception as e:
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def criar_fornecedor(cnpj, nome_fornecedor, endereco, email, telefone):
        session = Session()
        try:
            fornecedor_existente = session.query(Fornecedores).filter_by(cnpj=cnpj).first()

            if fornecedor_existente:
                return {"erro": "Já existe um fornecedor com esse CNPJ."}, 400

            novo_fornecedor = Fornecedores(
                cnpj=cnpj,
                nome_fornecedor=nome_fornecedor,
                endereco=endereco,
                email=email,
                telefone=telefone
            )

            session.add(novo_fornecedor)
            session.commit()

            return {"mensagem": "Fornecedor criado com sucesso."}, 201

        except Exception as e:
            session.rollback()
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def editar_fornecedor(cnpj, novo_nome=None, novo_endereco=None, novo_email=None, novo_telefone=None):
        session = Session()
        try:
            fornecedor = session.query(Fornecedores).filter_by(cnpj=cnpj).first()

            if not fornecedor:
                return {"erro": "Fornecedor não encontrado."}, 404

            if novo_nome is not None:
                fornecedor.nome_fornecedor = novo_nome
            if novo_endereco is not None:
                fornecedor.endereco = novo_endereco
            if novo_email is not None:
                fornecedor.email = novo_email
            if novo_telefone is not None:
                fornecedor.telefone = novo_telefone

            session.commit()
            return {"mensagem": "Fornecedor atualizado com sucesso."}, 200

        except Exception as e:
            session.rollback()
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

    @staticmethod
    def deletar_fornecedor(cnpj):
        session = Session()
        try:
            fornecedor = session.query(Fornecedores).filter_by(cnpj=cnpj).first()

            if not fornecedor:
                return {"erro": "Fornecedor não encontrado."}, 404

            session.delete(fornecedor)
            session.commit()
            return {"mensagem": "Fornecedor deletado com sucesso."}, 200

        except Exception as e:
            session.rollback()
            return {"erro": f"Erro inesperado: {str(e)}"}, 500

        finally:
            session.close()

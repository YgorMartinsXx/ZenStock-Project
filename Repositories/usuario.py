from database_connection import Session
from Model.classe_usuarios import Usuarios


class GerenciadorUsuarios:

    @staticmethod
    def login_usuario(login_usuario, senha):
        session = Session()
        try:
            usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
            if not usuario:
                return {"erro": "Usuário não encontrado."}, 404
            if usuario.senha != senha:
                return {"erro": "Senha incorreta."}, 401

            usuario_json = {
                "mensagem": "Login realizado com sucesso!",
                "login": usuario.login,
                "cargo": usuario.cargo
            }
            return usuario_json, 200
        except Exception as e:
            return {"erro": f"Erro no login: {str(e)}"}, 500
        finally:
            session.close()

    @staticmethod
    def buscar_usuario(login_usuario):
        session = Session()
        try:
            usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
            if not usuario:
                return {"erro": "Usuário não encontrado"}, 404

            fornecimento_json = [{
                "login": usuario.login,
                "cargo": usuario.cargo
            }]
            return fornecimento_json, 200
        except:
            return {"erro": "Erro, tente novamente"}, 500
        finally:
            session.close()

    @staticmethod
    def criar_usuario(login_usuario, senha, cargo):
        session = Session()
        cargos_validos = ['Estoquista', 'Administrador']
        try:
            usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
            if usuario:
                return {"erro": "Login em uso."}, 400

            if cargo not in cargos_validos:
                return {"erro": "Cargo não corresponde a nenhuma opção possível. Tente um cargo válido."}, 400

            novo_usuario = Usuarios(login=login_usuario, senha=senha, cargo=cargo)
            session.add(novo_usuario)
            session.commit()

            return {
                "mensagem": "Usuário criado com sucesso!",
                "login": novo_usuario.login,
                "cargo": novo_usuario.cargo
            }, 200
        except:
            session.rollback()
            return {"erro": "Erro: tente novamente"}, 500
        finally:
            session.close()

    @staticmethod
    def deleta_usuario(login_usuario):
        session = Session()
        try:
            usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
            if not usuario:
                return {"erro": "Usuário não encontrado"}, 404

            session.query(Usuarios).filter_by(login=login_usuario).delete()
            session.commit()

            fornecimento_json = [{
                "mensagem": "Usuário deletado com sucesso!",
                "login": usuario.login,
                "cargo": usuario.cargo
            }]
            return fornecimento_json, 200
        except:
            session.rollback()
            return {"erro": "Erro, tente novamente"}, 500
        finally:
            session.close()

    @staticmethod
    def alterar_senha(login_usuario, nova_senha):
        session = Session()
        try:
            usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
            if not usuario:
                return {"erro": "Usuário não encontrado."}, 404

            usuario.senha = nova_senha
            session.commit()

            return {"mensagem": "Senha alterada com sucesso."}, 200
        except Exception as e:
            session.rollback()
            return {"erro": f"Erro: {str(e)}"}, 500
        finally:
            session.close()

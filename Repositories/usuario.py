from database_connection import Session

from Model.classe_usuarios import Usuarios


def login_usuario(login_usuario, senha):
    session = Session()

    try:
        # Buscar usuário pelo login
        usuario = session.query(Usuarios).filter_by(login=login_usuario).first()

        if not usuario:
            return {"erro": "Usuário não encontrado."}, 404

        # Verifica a senha (simples, sem hash ainda)
        if usuario.senha != senha:
            return {"erro": "Senha incorreta."}, 401

        # Retorna os dados do usuário autenticado
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


def Buscar_usuario(login_usuario):
    session = Session()

    try:
        # Buscar o login do usuario 
        usuario = session.query(Usuarios).filter_by(login = login_usuario).first()
        if not usuario:
            return {"erro": "Usuario não encontrado"}, 404
        
        # Builda o formato a ser devolvido pela rota.
        fornecimento_json = [{

             "login": usuario.login, 
             "cargo": usuario.cargo

             }]
        
        return fornecimento_json, 200

    except:
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()


def criar_usuario(login_usuario, senha, cargo):
    session = Session()
    cargos = ['Estoquista', 'Administrador']
    try:
        
        # verifica se o usuario já existe no sistema.
        usuario = session.query(Usuarios).filter_by(login=login_usuario).first()
        if usuario:
            return {"erro": "Login em Uso."}, 400

        # Verifica se o cargo corresponde as opções
        if cargo not in cargos:
            return {"erro": "cargo não corresponde a nenhuma opção possivel. tente um cargo válido"}

        # Criar um novo usuario
        novo_usuario = Usuarios(login = login_usuario, senha = senha, cargo = cargo)
        session.add(novo_usuario)
        session.commit()  # Commit para gerar o usuario

        return {
            "mensagem": "Usuario criado com sucesso!",
            "login": novo_usuario.login,
            "cargo": novo_usuario.cargo
        }, 200

    except:
        session.rollback()
        return {"erro": "Erro: Tente novamente"}, 500
    
    finally:
        session.close()


def deleta_usuario(login_usuario):
    session = Session()

    try:
        # Buscar o login do usuario.
        usuario = session.query(Usuarios).filter_by(login = login_usuario).first()
        if not usuario:
            return {"erro": "Usuario não encontrado"}, 404
        
        # Deleta o Usuario.
        session.query(Usuarios).filter_by(login=login_usuario).delete()
        session.commit()
        
        # Builda o formato a ser devolvido pela rota.
        fornecimento_json = [{
             "Mensagem": "Usuario deletado com Sucesso!",
             "login": usuario.login,
             "cargo": usuario.cargo

             }]
        
        return fornecimento_json, 200

    except:
        session.rollback()
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()


def alterar_senha(login_usuario, nova_senha):
    session = Session()

    try:
        # Buscar o login do usuario.
        usuario = session.query(Usuarios).filter_by(login = login_usuario).first()
        if not usuario:
            return {"erro": "Usuário não encontrado."}, 404
        
        # Salva as mudanças no banco
        usuario.senha = nova_senha
        session.commit()

        return {"mensagem": "Senha alterada com sucesso."}, 200

    except Exception as e:
        session.rollback()
        return {"erro": f"Erro: {str(e)}"}, 500

    finally:
        session.close()
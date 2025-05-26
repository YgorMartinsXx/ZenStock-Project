from database_connection import Session
from Model.classe_movimenta import Movimenta

def buscar_movimentacao(id_pesquisado):
    session = Session()
    try:
        movimentacao = session.query(Movimenta).filter_by(id_movimentacao=int(id_pesquisado)).first()

        if not movimentacao:
            return {"erro": "Movimentação não encontrada."}, 404

        movimentacao_json = {
            "id_movimentacao": movimentacao.id_movimentacao,
            "evento": movimentacao.evento,
            "quantidade": movimentacao.quantidade,
            "data_movimentacao": movimentacao.data_movimentacao.isoformat() if movimentacao.data_movimentacao else None,
            "cod_produto": movimentacao.cod_produto,
            "usuario": movimentacao.usuario
        }

        return movimentacao_json, 200

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}, 500

    finally:
        session.close()


def todas_movimentacoes():
    session = Session()
    try:
        movimentacoes = session.query(Movimenta).all()

        if not movimentacoes:
            return {"erro": "Nenhuma movimentação encontrada."}, 404

        movimentacoes_json = [
            {
                "id_movimentacao": m.id_movimentacao,
                "evento": m.evento,
                "quantidade": m.quantidade,
                "data_movimentacao": m.data_movimentacao.isoformat() if m.data_movimentacao else None,
                "cod_produto": m.cod_produto,
                "usuario": m.usuario
            }
            for m in movimentacoes
        ]

        return movimentacoes_json, 200

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}, 500

    finally:
        session.close()


def movimentacoes_por_produto(cod_produto):
    session = Session()
    try:
        movimentacoes = session.query(Movimenta).filter_by(cod_produto=int(cod_produto)).all()

        if not movimentacoes:
            return {"erro": "Nenhuma movimentação encontrada para este produto."}, 404

        movimentacoes_json = [
            {
                "id_movimentacao": m.id_movimentacao,
                "evento": m.evento,
                "quantidade": m.quantidade,
                "data_movimentacao": m.data_movimentacao.isoformat() if m.data_movimentacao else None,
                "cod_produto": m.cod_produto,
                "usuario": m.usuario
            }
            for m in movimentacoes
        ]

        return movimentacoes_json, 200

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}, 500

    finally:
        session.close()


def movimentacoes_por_usuario(usuario):
    session = Session()
    try:
        movimentacoes = session.query(Movimenta).filter_by(usuario=usuario).all()

        if not movimentacoes:
            return {"erro": "Nenhuma movimentação encontrada para este usuário."}, 404

        movimentacoes_json = [
            {
                "id_movimentacao": m.id_movimentacao,
                "evento": m.evento,
                "quantidade": m.quantidade,
                "data_movimentacao": m.data_movimentacao.isoformat() if m.data_movimentacao else None,
                "cod_produto": m.cod_produto,
                "usuario": m.usuario
            }
            for m in movimentacoes
        ]

        return movimentacoes_json, 200

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}, 500

    finally:
        session.close()


def criar_movimentacao(evento, quantidade, cod_produto, usuario, data_movimentacao=None):
    session = Session()
    try:
        nova_movimentacao = Movimenta(
            evento=evento,
            quantidade=quantidade,
            cod_produto=cod_produto,
            usuario=usuario,
            data_movimentacao=data_movimentacao  # pode ser None, aí o default do BD ou SQLAlchemy entra
        )
        session.add(nova_movimentacao)
        session.commit()
        return {"mensagem": "Movimentação criada com sucesso.", "id_movimentacao": nova_movimentacao.id_movimentacao}, 201

    except Exception as e:
        session.rollback()
        return {"erro": f"Erro inesperado: {str(e)}"}, 500

    finally:
        session.close()


def editar_movimentacao(id_movimentacao, novo_evento=None, nova_quantidade=None, novo_cod_produto=None, novo_usuario=None, nova_data_movimentacao=None):
    session = Session()
    try:
        movimentacao = session.query(Movimenta).filter_by(id_movimentacao=int(id_movimentacao)).first()

        if not movimentacao:
            return {"erro": "Movimentação não encontrada."}, 404

        if novo_evento is not None:
            movimentacao.evento = novo_evento
        if nova_quantidade is not None:
            movimentacao.quantidade = nova_quantidade
        if novo_cod_produto is not None:
            movimentacao.cod_produto = novo_cod_produto
        if novo_usuario is not None:
            movimentacao.usuario = novo_usuario
        if nova_data_movimentacao is not None:
            movimentacao.data_movimentacao = nova_data_movimentacao

        session.commit()
        return {"mensagem": "Movimentação atualizada com sucesso."}, 200

    except Exception as e:
        session.rollback()
        return {"erro": f"Erro inesperado: {str(e)}"}, 500

    finally:
        session.close()


def deletar_movimentacao(id_movimentacao):
    session = Session()
    try:
        movimentacao = session.query(Movimenta).filter_by(id_movimentacao=int(id_movimentacao)).first()

        if not movimentacao:
            return {"erro": "Movimentação não encontrada."}, 404

        session.delete(movimentacao)
        session.commit()
        return {"mensagem": "Movimentação deletada com sucesso."}, 200

    except Exception as e:
        session.rollback()
        return {"erro": f"Erro inesperado: {str(e)}"}, 500

    finally:
        session.close()
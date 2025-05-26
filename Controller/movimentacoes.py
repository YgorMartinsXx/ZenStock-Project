from flask import Blueprint, request, jsonify
from Repositories.movimentacoes import (
    buscar_movimentacao,
    todas_movimentacoes,
    movimentacoes_por_produto,
    movimentacoes_por_usuario,
    criar_movimentacao,
    editar_movimentacao,
    deletar_movimentacao
)

movimentacoes_bp = Blueprint('movimentacoes', __name__, url_prefix='/movimentacoes')

# Rota para buscar todas as movimentações
@movimentacoes_bp.route('/', methods=['GET'])
def get_todas_movimentacoes():
    return todas_movimentacoes()

# Rota para buscar movimentação por ID
@movimentacoes_bp.route('/<int:id_movimentacao>', methods=['GET'])
def get_movimentacao(id_movimentacao):
    return buscar_movimentacao(id_movimentacao)

# Rota para buscar movimentações por produto
@movimentacoes_bp.route('/produto/<int:cod_produto>', methods=['GET'])
def get_movimentacoes_produto(cod_produto):
    return movimentacoes_por_produto(cod_produto)

# Rota para buscar movimentações por usuário
@movimentacoes_bp.route('/usuario/<usuario>', methods=['GET'])
def get_movimentacoes_usuario(usuario):
    return movimentacoes_por_usuario(usuario)

# Rota para criar uma nova movimentação
@movimentacoes_bp.route('/', methods=['POST'])
def post_movimentacao():
    data = request.get_json()
    evento = data.get('evento')
    quantidade = data.get('quantidade')
    cod_produto = data.get('cod_produto')
    usuario = data.get('usuario')
    data_movimentacao = data.get('data_movimentacao')  # opcional

    if not evento or quantidade is None or not cod_produto or not usuario:
        return jsonify({"erro": "Campos obrigatórios: evento, quantidade, cod_produto, usuario"}), 400

    return criar_movimentacao(evento, quantidade, cod_produto, usuario, data_movimentacao)

# Rota para editar uma movimentação existente
@movimentacoes_bp.route('/<int:id_movimentacao>', methods=['PUT'])
def put_movimentacao(id_movimentacao):
    data = request.get_json()
    novo_evento = data.get('evento')
    nova_quantidade = data.get('quantidade')
    novo_cod_produto = data.get('cod_produto')
    novo_usuario = data.get('usuario')
    nova_data_movimentacao = data.get('data_movimentacao')

    return editar_movimentacao(
        id_movimentacao,
        novo_evento,
        nova_quantidade,
        novo_cod_produto,
        novo_usuario,
        nova_data_movimentacao
    )

# Rota para deletar uma movimentação
@movimentacoes_bp.route('/<int:id_movimentacao>', methods=['DELETE'])
def delete_movimentacao(id_movimentacao):
    return deletar_movimentacao(id_movimentacao)
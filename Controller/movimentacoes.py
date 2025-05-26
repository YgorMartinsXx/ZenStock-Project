from flask import Blueprint, request, jsonify
from Repositories.movimentacoes import GerenciadorMovimentacoes

movimentacoes_bp = Blueprint('movimentacoes', __name__, url_prefix='/movimentacoes')

@movimentacoes_bp.route('/', methods=['GET'])
def get_todas_movimentacoes():
    resultado, status = GerenciadorMovimentacoes.todas_movimentacoes()
    return jsonify(resultado), status

@movimentacoes_bp.route('/<int:id_movimentacao>', methods=['GET'])
def get_movimentacao(id_movimentacao):
    resultado, status = GerenciadorMovimentacoes.buscar_movimentacao(id_movimentacao)
    return jsonify(resultado), status

@movimentacoes_bp.route('/produto/<int:cod_produto>', methods=['GET'])
def get_movimentacoes_produto(cod_produto):
    resultado, status = GerenciadorMovimentacoes.movimentacoes_por_produto(cod_produto)
    return jsonify(resultado), status

@movimentacoes_bp.route('/usuario/<usuario>', methods=['GET'])
def get_movimentacoes_usuario(usuario):
    resultado, status = GerenciadorMovimentacoes.movimentacoes_por_usuario(usuario)
    return jsonify(resultado), status

@movimentacoes_bp.route('/', methods=['POST'])
def post_movimentacao():
    data = request.get_json()
    evento = data.get('evento')
    quantidade = data.get('quantidade')
    cod_produto = data.get('cod_produto')
    usuario = data.get('usuario')
    data_movimentacao = data.get('data_movimentacao')

    if not evento or quantidade is None or not cod_produto or not usuario:
        return jsonify({"erro": "Campos obrigatórios: evento, quantidade, cod_produto, usuario"}), 400

    resultado, status = GerenciadorMovimentacoes.criar_movimentacao(
        evento, quantidade, cod_produto, usuario, data_movimentacao
    )
    return jsonify(resultado), status

@movimentacoes_bp.route('/<int:id_movimentacao>', methods=['PUT'])
def put_movimentacao(id_movimentacao):
    data = request.get_json()
    novo_evento = data.get('evento')
    nova_quantidade = data.get('quantidade')
    novo_cod_produto = data.get('cod_produto')
    novo_usuario = data.get('usuario')
    nova_data_movimentacao = data.get('data_movimentacao')

    resultado, status = GerenciadorMovimentacoes.editar_movimentacao(
        id_movimentacao,
        novo_evento,
        nova_quantidade,
        novo_cod_produto,
        novo_usuario,
        nova_data_movimentacao
    )
    return jsonify(resultado), status

@movimentacoes_bp.route('/<int:id_movimentacao>', methods=['DELETE'])
def delete_movimentacao(id_movimentacao):
    resultado, status = GerenciadorMovimentacoes.deletar_movimentacao(id_movimentacao)
    return jsonify(resultado), status

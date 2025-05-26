from flask import Blueprint, request, jsonify
from Repositories.pedido import GerenciadorPedidos

# Criando a Blueprint para pedidos
pedidos_bp = Blueprint('pedidos', __name__, url_prefix='/pedidos')

# Rota para buscar todos os pedidos
@pedidos_bp.route('/', methods=['GET'])
def get_pedidos():
    resultado, status = GerenciadorPedidos.todos_pedidos()
    return jsonify(resultado), status

# Rota para buscar um pedido específico
@pedidos_bp.route('/<int:id_pedido>', methods=['GET'])
def get_pedido(id_pedido):
    resultado, status = GerenciadorPedidos.buscar_pedido(id_pedido)
    return jsonify(resultado), status

# Rota para criar um novo pedido
@pedidos_bp.route('/', methods=['POST'])
def post_pedido():
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Dados inválidos ou ausentes"}), 400

    cnpj_fornecedor = data.get('cnpj_fornecedor')
    cod_produto = data.get('cod_produto')
    quantidade_fornecida = data.get('quantidade')
    login_usuario = data.get('usuario')

    resultado, status = GerenciadorPedidos.criar_pedido(
        cnpj_fornecedor, cod_produto, quantidade_fornecida, login_usuario
    )
    return jsonify(resultado), status

# Rota para excluir um pedido
@pedidos_bp.route('/excluir/<int:id_pedido>', methods=['DELETE'])
def delete_pedido(id_pedido):
    resultado, status = GerenciadorPedidos.excluir_pedido(id_pedido)
    return jsonify(resultado), status

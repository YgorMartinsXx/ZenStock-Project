from flask import Blueprint, request, jsonify
from Repositories.fornece import (
    buscar_fornecimento, todos_fornecimentos, fornecimento_por_produto,
    fornecimento_por_fornecedor, deleta_fornecimento, editar_fornecimento
)

fornecimento_bp = Blueprint('fornecimento', __name__, url_prefix='/fornecimento')

# Rota para buscar todos os fornecimentos
@fornecimento_bp.route('/', methods=['GET'])
def get_todos_fornecimentos():
    return jsonify(todos_fornecimentos())

# Rota para buscar um fornecimento específico
@fornecimento_bp.route('/<int:id_pedido>', methods=['GET'])
def get_fornecimento(id_pedido):
    return jsonify(buscar_fornecimento(id_pedido))

# Rota para buscar fornecimentos por produto
@fornecimento_bp.route('/produto/<int:codigo_produto>', methods=['GET'])
def get_fornecimento_por_produto(codigo_produto):
    return jsonify(fornecimento_por_produto(codigo_produto))

# Rota para buscar fornecimentos por fornecedor
@fornecimento_bp.route('/fornecedor/<string:cnpj_fornecedor>', methods=['GET'])
def get_fornecimento_por_fornecedor(cnpj_fornecedor):
    return jsonify(fornecimento_por_fornecedor(cnpj_fornecedor))

# Rota para excluir um fornecimento
@fornecimento_bp.route('/<int:id_pedido>', methods=['DELETE'])
def delete_fornecimento(id_pedido):
    return jsonify(deleta_fornecimento(id_pedido))

# Rota para editar um fornecimento
@fornecimento_bp.route('/<int:id_pedido>', methods=['PUT'])
def update_fornecimento(id_pedido):
    data = request.get_json()
    novo_cnpj = data.get('cnpj_fornecedor')
    novo_cod_produto = data.get('cod_produto')
    nova_quantidade = data.get('quantidade')
    
    return jsonify(editar_fornecimento(id_pedido, novo_cnpj, novo_cod_produto, nova_quantidade))

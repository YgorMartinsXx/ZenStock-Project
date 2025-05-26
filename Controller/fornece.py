from flask import Blueprint, request, jsonify
from Repositories.fornece import GerenciadorFornecimentos

fornecimento_bp = Blueprint('fornecimento', __name__, url_prefix='/fornecimento')

# GET - Buscar todos os fornecimentos
@fornecimento_bp.route('/', methods=['GET'])
def get_todos_fornecimentos():
    resposta, status = GerenciadorFornecimentos.todos_fornecimentos()
    return jsonify(resposta), status

# GET - Buscar fornecimento por ID do pedido
@fornecimento_bp.route('/<int:id_pedido>', methods=['GET'])
def get_fornecimento(id_pedido):
    resposta, status = GerenciadorFornecimentos.buscar_fornecimento(id_pedido)
    return jsonify(resposta), status

# GET - Buscar fornecimentos por código do produto
@fornecimento_bp.route('/produto/<int:codigo_produto>', methods=['GET'])
def get_fornecimento_por_produto(codigo_produto):
    resposta, status = GerenciadorFornecimentos.fornecimento_por_produto(codigo_produto)
    return jsonify(resposta), status

# GET - Buscar fornecimentos por CNPJ do fornecedor
@fornecimento_bp.route('/fornecedor/<string:cnpj_fornecedor>', methods=['GET'])
def get_fornecimento_por_fornecedor(cnpj_fornecedor):
    resposta, status = GerenciadorFornecimentos.fornecimento_por_fornecedor(cnpj_fornecedor)
    return jsonify(resposta), status

# DELETE - Deletar fornecimento por ID do pedido
@fornecimento_bp.route('/<int:id_pedido>', methods=['DELETE'])
def delete_fornecimento(id_pedido):
    resposta, status = GerenciadorFornecimentos.deleta_fornecimento(id_pedido)
    return jsonify(resposta), status

# PUT - Editar fornecimento
@fornecimento_bp.route('/<int:id_pedido>', methods=['PUT'])
def update_fornecimento(id_pedido):
    data = request.get_json()
    novo_cnpj = data.get('cnpj_fornecedor')
    novo_cod_produto = data.get('cod_produto')
    nova_quantidade = data.get('quantidade')

    resposta, status = GerenciadorFornecimentos.editar_fornecimento(
        id_pedido=id_pedido,
        novo_cnpj=novo_cnpj,
        novo_cod_produto=novo_cod_produto,
        nova_quantidade=nova_quantidade
    )
    return jsonify(resposta), status

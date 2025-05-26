from flask import Blueprint, request, jsonify
from Repositories.fornecedores import (
    buscar_fornecedor,
    todos_fornecedores,
    criar_fornecedor,
    editar_fornecedor,
    deletar_fornecedor
)

fornecedores_bp = Blueprint('fornecedores', __name__, url_prefix='/fornecedores')

# Rota para buscar todos os fornecedores
@fornecedores_bp.route('/', methods=['GET'])
def get_todos_fornecedores():
    return todos_fornecedores()

# Rota para buscar um fornecedor pelo CNPJ
@fornecedores_bp.route('/<cnpj>', methods=['GET'])
def get_fornecedor(cnpj):
    return buscar_fornecedor(cnpj)

# Rota para criar um novo fornecedor
@fornecedores_bp.route('/', methods=['POST'])
def post_fornecedor():
    data = request.get_json()
    cnpj = data.get('cnpj')
    nome = data.get('nome_fornecedor')
    endereco = data.get('endereco')
    email = data.get('email')
    telefone = data.get('telefone')

    if not cnpj or not nome or not endereco or not email or not telefone:
        return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

    return criar_fornecedor(cnpj, nome, endereco, email, telefone)

# Rota para editar um fornecedor pelo CNPJ
@fornecedores_bp.route('/<cnpj>', methods=['PUT'])
def put_fornecedor(cnpj):
    data = request.get_json()
    novo_nome = data.get('nome_fornecedor')
    novo_endereco = data.get('endereco')
    novo_email = data.get('email')
    novo_telefone = data.get('telefone')

    return editar_fornecedor(
        cnpj,
        novo_nome,
        novo_endereco,
        novo_email,
        novo_telefone
    )

# Rota para deletar um fornecedor pelo CNPJ
@fornecedores_bp.route('/<cnpj>', methods=['DELETE'])
def delete_fornecedor(cnpj):
    return deletar_fornecedor(cnpj)
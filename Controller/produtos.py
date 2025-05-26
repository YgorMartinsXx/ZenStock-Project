from flask import Blueprint, request
from flasgger import swag_from
from Repositories.produtos import GerenciadorProdutos

produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/produtos', methods=['GET'])
@swag_from({
    'tags': ['Produtos'],
    'description': 'Busca produtos por categoria, ID, nome ou preço.',
    'parameters': [
        {'name': 'cod_produto', 'in': 'query', 'type': 'integer', 'description': 'ID do produto a ser buscado.'},
        {'name': 'categoria', 'in': 'query', 'type': 'string', 'description': 'Categoria do produto a ser buscado.'},
        {'name': 'nome_produto', 'in': 'query', 'type': 'string', 'description': 'Nome do produto a ser buscado.'},
        {'name': 'preco_minimo', 'in': 'query', 'type': 'number', 'description': 'Preço mínimo do produto.'},
        {'name': 'preco_maximo', 'in': 'query', 'type': 'number', 'description': 'Preço máximo do produto.'},
        {'name': 'ordenacao_preco', 'in': 'query', 'type': 'string', 'description': 'Ordenação do preço ("crescente" ou "decrescente").'},
        {'name': 'completo', 'in': 'query', 'type': 'string', 'description': 'Retorna todos os produtos, use "true".'}
    ],
    'responses': {
        '200': {'description': 'Lista de produtos encontrados.'},
        '400': {'description': 'Argumento inválido.'},
        '404': {'description': 'Nenhum produto encontrado.'},
        '500': {'description': 'Erro ao acessar o banco de dados.'}
    }
})
def get_produtos():
    return GerenciadorProdutos.buscar_produtos(request.args)


@produtos_bp.route('/produtos/<cod_produto>', methods=['DELETE'])
@swag_from({
    'tags': ['Produtos'],
    'description': 'Deleta um produto pelo cod_produto.',
    'parameters': [
        {'name': 'cod_produto', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do produto a ser deletado.'}
    ],
    'responses': {
        '200': {'description': 'Produto deletado com sucesso.'},
        '400': {'description': 'cod_produto não fornecido ou inválido.'},
        '404': {'description': 'Produto não encontrado.'},
        '500': {'description': 'Erro interno ao deletar produto.'}
    }
})
def delete_produto(cod_produto):
    return GerenciadorProdutos.deletar_produto(cod_produto)


@produtos_bp.route('/produtos/<cod_produto>', methods=['PUT'])
@swag_from({
    'tags': ['Produtos'],
    'description': 'Edita um produto existente pelo cod_produto.',
    'parameters': [
        {'name': 'cod_produto', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID do produto a ser editado.'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome_produto': {'type': 'string', 'description': 'Novo nome do produto.'},
                    'categoria': {'type': 'string', 'description': 'Nova categoria do produto.'},
                    'descricao': {'type': 'string', 'description': 'Nova descrição do produto.'},
                    'preco_unitario': {'type': 'number', 'description': 'Novo preço unitário do produto.'}
                }
            },
            'description': 'Dados do produto a serem atualizados (não é possível alterar aqui a quantidade).'
        }
    ],
    'responses': {
        '200': {'description': 'Produto atualizado com sucesso.'},
        '400': {'description': 'cod_produto não fornecido ou inválido, ou dados de produto inválidos.'},
        '404': {'description': 'Produto não encontrado.'},
        '500': {'description': 'Erro interno ao editar produto.'}
    }
})
def edit_produto(cod_produto):
    return GerenciadorProdutos.editar_produto(cod_produto)


@produtos_bp.route('/produtos', methods=['POST'])
@swag_from({
    'tags': ['Produtos'],
    'description': 'Cadastra um novo produto.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'cod_produto': {'type': 'integer', 'description': 'Código do produto.'},
                    'nome_produto': {'type': 'string', 'description': 'Nome do produto.'},
                    'categoria': {'type': 'string', 'description': 'Categoria do produto.'},
                    'descricao': {'type': 'string', 'description': 'Descrição do produto (opcional).'},
                    'preco_unitario': {'type': 'number', 'description': 'Preço unitário do produto.'},
                    'quantidade': {'type': 'integer', 'description': 'Quantidade em estoque.'}
                },
                'required': ['cod_produto', 'nome_produto', 'categoria', 'preco_unitario', 'quantidade']
            }
        }
    ],
    'responses': {
        '201': {'description': 'Produto cadastrado com sucesso.'},
        '400': {'description': 'Dados do produto incompletos ou inválidos.'},
        '500': {'description': 'Erro interno ao cadastrar produto.'}
    }
})
def post_produto():
    return GerenciadorProdutos.cadastrar_produto()

from flask import jsonify
from Model.classe_produtos import Produto
from database_connection import db # Será necessário refazer a conexão SQL do arquivo mencionado

def buscar_produtos(args):
    """Busca produtos por categoria, ID, nome, ou preço."""

    # Filtro de busca inicial: todos os produtos
    query = Produto.query

    # Filtro por ID
    id = args.get('id')
    if id:
        if not id.isdigit():
            return jsonify({'message': 'O ID fornecido deve ser um número inteiro.'}), 400
        
        produto = Produto.query.get(id)
        if produto:
            return jsonify(produto.to_dict())  # Converte o produto para dicionário e retorna como JSON
        else:
            return jsonify({'message': 'Nenhum produto encontrado com o ID fornecido.'}), 404

    # Filtro por categoria
    categoria = args.get('categoria')
    if categoria:
        if categoria.isdigit():
            return jsonify({'message': 'A categoria deve ser uma string.'}), 400
        query = query.filter(Produto.categoria == categoria)

    # Filtro por nome
    nome = args.get('nome')
    if nome:
        if nome.isdigit():
            return jsonify({'message': 'O nome fornecido deve ser uma string.'}), 400
        query = query.filter(Produto.nome_produto.like(f"%{nome}%"))

    # Filtro por preço (mínimo e máximo)
    preco_minimo = args.get('preco_minimo')
    if preco_minimo:
        try:
            preco_minimo = float(preco_minimo)
            query = query.filter(Produto.preco_unitario >= preco_minimo)
        except ValueError:
            return jsonify({'message': 'Preço mínimo inválido.'}), 400

    preco_maximo = args.get('preco_maximo')
    if preco_maximo:
        try:
            preco_maximo = float(preco_maximo)
            query = query.filter(Produto.preco_unitario <= preco_maximo)
        except ValueError:
            return jsonify({'message': 'Preço máximo inválido.'}), 400

    # Filtro por ordenação (preço crescente ou decrescente)
    preco_crescente = args.get('preco')
    if preco_crescente:
        if preco_crescente.lower() == 'true':
            query = query.order_by(Produto.preco_unitario.asc())  # Ordena de forma crescente
        elif preco_crescente.lower() == 'false':
            query = query.order_by(Produto.preco_unitario.desc())  # Ordena de forma decrescente
        else:
            return jsonify({'message': 'Valor inválido para ordenação de preço.'}), 400

    # Executa a consulta e converte os resultados para uma lista
    produtos = query.all()

    if produtos:
        # Converte cada produto em um dicionário e retorna como JSON
        return jsonify([produto.to_dict() for produto in produtos])
    else:
        return jsonify({'message': 'Nenhum produto encontrado com os parâmetros informados.'}), 404

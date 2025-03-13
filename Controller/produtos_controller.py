from flask import jsonify
from Mocks.produtos_mock import produtos_dict # deverá ser substituído futuramente pelos dados do banco de dados

def buscar_produtos(args):
    """Busca produtos por categoria, ID ou nome."""

    if not produtos_dict:
        return jsonify({'message': 'A lista de produtos está vazia.'}), 404
    
    categoria = args.get('categoria')
    id = args.get('id')
    nome = args.get('nome')
    preco_minimo = args.get('preco_minimo')
    preco_maximo = args.get('preco_maximo')
    preco_crescente = args.get('preco')

    resultados = list(produtos_dict.values())

    # Caso um ID seja fornecido, busca diretamente pelo identificador único
    if id:
        if not id.isdigit():
            return jsonify({'message': 'O ID fornecido deve ser um número inteiro.'}), 400
        
        id = int(id)
        produto = next((p for p in produtos_dict.values() if p['cod_produto'] == id), None)
        if produto: return jsonify(produto)
        else: return jsonify({'message': 'Nenhum produto encontrado com os parâmetros informados.'}), 404

    try:
        # Filtros de limites de preço
        if preco_minimo:
            preco_minimo = float(preco_minimo)
            resultados = [produto for produto in resultados if produto['preco_unitario'] >= preco_minimo]
        if preco_maximo:
            preco_maximo = float(preco_maximo)
            resultados = [produto for produto in resultados if produto['preco_unitario'] <= preco_maximo]
        # Filtro de ordenação por preço
        if preco_crescente:
            resultados.sort(key=lambda p: p['preco_unitario'], reverse=preco_crescente.lower() == 'false')
    except ValueError:
        return jsonify({'message': 'Filtros de preço inválidos.'}), 400

    # Aplicação de filtros por categoria e nome sem quebrar outros filtros
    if categoria:
        if categoria.isdigit():
            return jsonify({'message': 'A categoria deve ser uma string.'}), 400
        resultados = [p for p in resultados if p['categoria'] == categoria]
    if nome:
        if nome.isdigit():
            return jsonify({'message': 'O nome fornecido deve ser uma string.'}), 400
        resultados = [p for p in resultados if p['nome'] == nome]

    if resultados:
        return jsonify(resultados)
    else:
        return jsonify({'message': 'Nenhum produto encontrado com os parâmetros informados.'}), 404
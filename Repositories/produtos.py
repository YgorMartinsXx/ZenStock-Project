from flask import jsonify, request
from decimal import Decimal
from database_connection import Session
from Model.classe_produtos import Produto

def buscar_produtos(args=None):
    """Busca produtos por categoria, ID, nome ou preço usando SQLAlchemy."""
    
    session = Session()
    
    try:
        # Obtém os argumentos da requisição
        if args is None:
            args = request.args

        # Verifica se pelo menos um argumento foi fornecido
        if not args:
            return jsonify({'message': 'Argumento inválido.'}), 400

        # Começa a query base
        query = session.query(Produto)

        # Filtro 'completo' (retorna todos os produtos)
        completo = args.get('completo')
        if completo:
            if completo.lower() != 'true':
                return jsonify({'message': 'O parâmetro deve ser apenas "true" para retornar todos os produtos.'}), 404
            # Não aplica filtros específicos, apenas retorna todos os produtos
            pass  # A consulta continuará sem filtros adicionais

        # Filtro por cod_produto
        cod_produto = args.get('cod_produto')
        if cod_produto:
            if not cod_produto.isdigit():
                return jsonify({'message': 'O cod_produto fornecido deve ser um número inteiro.'}), 400
            produto = query.filter(Produto.cod_produto == int(cod_produto)).first()
            session.close()
            if produto:
                return jsonify(produto.to_dict())  # serializa objeto
            return jsonify({'message': 'Nenhum produto encontrado com o ID fornecido.'}), 404

        # Filtro por categoria
        categoria = args.get('categoria')
        if categoria:
            if categoria.isdigit():
                return jsonify({'message': 'A categoria deve ser uma string.'}), 400
            query = query.filter(Produto.categoria == categoria)

        # Filtro por nome_produto
        nome_produto = args.get('nome_produto')
        if nome_produto:
            if nome_produto.isdigit():
                return jsonify({'message': 'O nome_produto fornecido deve ser uma string.'}), 400
            query = query.filter(Produto.nome_produto.ilike(f"%{nome_produto}%"))

        # filtrando por preço (converte para Decimal para garantir precisão)
        preco_minimo = args.get('preco_minimo')
        if preco_minimo:
            try:
                preco_minimo = Decimal(preco_minimo)
                query = query.filter(Produto.preco_unitario >= preco_minimo)
            except ValueError:
                return jsonify({'message': 'Preço mínimo inválido.'}), 400

        preco_maximo = args.get('preco_maximo')
        if preco_maximo:
            try:
                preco_maximo = Decimal(preco_maximo)
                query = query.filter(Produto.preco_unitario <= preco_maximo)
            except ValueError:
                return jsonify({'message': 'Preço máximo inválido.'}), 400

        # Ordenação por preço (crescente ou decrescente)
        ordenacao_preco = args.get('ordenacao_preco')
        if ordenacao_preco:
            if ordenacao_preco.lower() == 'crescente':
                query = query.order_by(Produto.preco_unitario.asc())
            elif ordenacao_preco.lower() == 'decrescente':
                query = query.order_by(Produto.preco_unitario.desc())
            else:
                return jsonify({'message': 'Valor inválido para ordenação de preço. Use "crescente" ou "decrescente".'}), 400

        produtos = query.all()
        session.close()

        #retorna os produtos encontrados com preco_unitario convertido para decimal se necessário
        if produtos:
            return jsonify([{
                **produto.to_dict(),
                'preco_unitario': float(produto.preco_unitario)  # Garantir que o preco_unitario seja um número float
            } for produto in produtos])
        else:
            return jsonify({'message': 'Nenhum produto encontrado com os parâmetros informados.'}), 404

    except Exception as e:
        session.rollback()
        return jsonify({'message': f'Erro ao acessar o banco de dados: {str(e)}'}), 500


def deletar_produto(cod_produto):
    """Deleta um produto do banco de dados pelo cod_produto."""

    session = Session()

    try: # se cod_produto nao for fornecido
        if not cod_produto:
            return jsonify({'message': 'cod_produto não fornecido.'}), 400

        if not cod_produto.isdigit(): # se é do tipo inteiro
            return jsonify({'message': 'O cod_produto deve ser um número inteiro.'}), 400

        cod_produto = int(cod_produto)

        # faz a busca
        produto = session.query(Produto).filter(Produto.cod_produto == cod_produto).first()

        # verifica se existe algum item com o cod fornecido
        if not produto:
            session.close()
            return jsonify({'message': 'Produto não encontrado.'}), 404

        # por fim, deleta o produto
        session.delete(produto)
        session.commit()
        session.close()

        return jsonify({'message': 'Produto deletado com sucesso.'}), 200

    except Exception as e: # caso haja algum erro interno do servidor
        session.rollback()
        session.close()
        return jsonify({'message': f'Erro ao deletar produto: {str(e)}'}), 500


def editar_produto(cod_produto):
    """Edita um produto existente no banco de dados, exceto a quantidade (regra de negócio)."""

    session = Session()

    try:
        # verifica se o codigo foi fornecido
        if not cod_produto:
            return jsonify({'message': 'cod_produto não fornecido.'}), 400

        # verifica se é int
        if not cod_produto.isdigit():
            return jsonify({'message': 'O cod_produto deve ser um número inteiro.'}), 400

        cod_produto = int(cod_produto)

        # buscando produto pelo codigo
        produto = session.query(Produto).filter(Produto.cod_produto == cod_produto).first()

        # verifica se existe
        if not produto:
            session.close()
            return jsonify({'message': 'Produto não encontrado.'}), 404

        # dados em json
        dados_produto = request.get_json()

        # atualiza os dados
        if dados_produto:
            if 'nome_produto' in dados_produto:
                produto.nome_produto = dados_produto['nome_produto']
            if 'categoria' in dados_produto:
                produto.categoria = dados_produto['categoria']
            if 'descricao' in dados_produto:
                produto.descricao = dados_produto['descricao']
            if 'preco_unitario' in dados_produto:
                try:
                    produto.preco_unitario = Decimal(dados_produto['preco_unitario'])
                except ValueError:
                    return jsonify({'message': 'Preço unitário inválido.'}), 400

            session.commit()
            session.close()

            return jsonify({'message': 'Produto atualizado com sucesso.'}), 200

        else:
            session.close()
            return jsonify({'message': 'Nenhum dado de produto fornecido para atualização.'}), 400

    except Exception as e: # erro interno
        session.rollback()
        session.close()
        return jsonify({'message': f'Erro interno ao editar produto: {str(e)}'}), 500
    

def cadastrar_produto():
    """Cadastra um novo produto no banco de dados."""

    session = Session()

    try:
        dados_produto = request.get_json()

        # verifica se todos os dados foram fornecidos
        if not dados_produto:
            return jsonify({'message': 'Dados do produto não fornecidos.'}), 400

        # valida dados do produto
        campos_obrigatorios = ['cod_produto', 'nome_produto', 'categoria', 'preco_unitario', 'quantidade']
        if not all(campo in dados_produto for campo in campos_obrigatorios):
            return jsonify({'message': 'Dados do produto incompletos.'}), 400

        # cria um novo objeto Produto com os dados fornecidos
        novo_produto = Produto(
            cod_produto=dados_produto['cod_produto'],
            nome_produto=dados_produto['nome_produto'],
            categoria=dados_produto['categoria'],
            descricao=dados_produto.get('descricao'),
            preco_unitario=Decimal(dados_produto['preco_unitario']),
            quantidade=dados_produto['quantidade']
        )

        # adiciona o produto ao db
        session.add(novo_produto)
        session.commit()
        session.close()

        return jsonify({'message': 'Produto cadastrado com sucesso.'}), 201

    # erros
    except ValueError:
        session.rollback()
        session.close()
        return jsonify({'message': 'Preço unitário inválido.'}), 400

    except Exception as e:
        session.rollback()
        session.close()
        return jsonify({'message': f'Erro interno ao cadastrar produto: {str(e)}'}), 500
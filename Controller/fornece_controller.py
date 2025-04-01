from database_connection import Session
from Model.classe_produtos import Produto
from Model.classe_fornecedores import Fornecedores
from Model.classe_fornece import Fornece


def buscar_fornecimento(id_pesquisado):
    session = Session()

    try:
        # Buscar o ID do pedido relacionado ao fornecimento
        fornecimento = session.query(Fornece).filter_by(id_Pedido=int(id_pesquisado)).first()
        if not fornecimento:
            return {"erro": "Fornecimento não encontrado"}, 404
        
        # Builda o formato a ser devolvido pela rota.
        fornecimento_json = [{

             "id_Pedido": fornecimento.id_Pedido, 
             "cnpj_fornecedor": fornecimento.cnpj_fornecedor,
             "cod_produto": fornecimento.cod_produto,
             "quantidade": fornecimento.quantidade

             }]
        
        return fornecimento_json, 200

    except:
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()


def todos_fornecimentos(id_pesquisado):
    session = Session()

    try:
        # Buscar todos os fornecimentos
        fornecimentos = session.query(Fornece).all()
        
        if not fornecimentos:
            return {"erro": "Fornecimento não encontrado"}, 404
        
        # Builda o formato a ser devolvido pela rota.
        fornecimento_json = [

            {
             "id_Pedido": fornecimentos.id_Pedido, 
             "cnpj_fornecedor": fornecimentos.cnpj_fornecedor,
             "cod_produto": fornecimentos.cod_produto,
             "quantidade": fornecimentos.quantidade,
             }

             for fornecimento in fornecimentos

             ]
        
        return fornecimento_json,200

    except:
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()


def fornecimento_por_produto(codigo_produto):
    session = Session()

    try:
        # Busca os fornecimentos de um produto especifico.
        fornecimentos = session.query(Fornece).filter_by(cod_produto = int(codigo_produto))
        
        # Builda o formato a ser devolvido pela rota.
        fornecimento_json = [

            {
             "id_Pedido": fornecimentos.id_Pedido, 
             "cnpj_fornecedor": fornecimentos.cnpj_fornecedor,
             "cod_produto": fornecimentos.cod_produto,
             "quantidade": fornecimentos.quantidade,
             }

             for fornecimento in fornecimentos

             ]
        
    except:
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()


def fornecimento_por_fornecedor(cnpj_fornecedor):
    session = Session()

    try:
        # Busca os fornecimentos de um fornecedor especifico.
        fornecimentos = session.query(Fornece).filter_by(cnpj = cnpj_fornecedor)
        
        # Builda o formato a ser devolvido pela rota.
        fornecimento_json = [
    
            {
             "id_Pedido": fornecimentos.id_Pedido, 
             "cnpj_fornecedor": fornecimentos.cnpj_fornecedor,
             "cod_produto": fornecimentos.cod_produto,
             "quantidade": fornecimentos.quantidade,
             }

             for fornecimento in fornecimentos

             ]
        
        return fornecimento_json, 200

    except:
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()


def deleta_fornecimento (id_pesquisado):

    session = Session()

    try:
        # Buscar o id do pedido
        pedido = session.query(Fornece).filter_by(id_Pedido = int(id_pesquisado)).first()
        if not pedido:
            return {"erro": "pedido não encontrado"}, 404
        
         # Removendo na tabela FORNECE
        session.query(Fornece).filter_by(id_pedido=int(id_pesquisado)).delete()
        session.commit()

    except:
        session.rollback()
        return {"erro": "Erro, tente novamente"}, 500
    
    finally:
        session.close()

    
    
def editar_fornecimento(id_pedido = None , novo_cnpj = None, novo_cod_produto = None, nova_quantidade = None):
    session = Session()

    try:
        # Buscar o fornecimento na tabela FORNECE
        fornecimento = session.query(Fornece).filter_by(id_Pedido=int(id_pedido)).first()
        if not fornecimento:
            return {"erro": "Fornecimento não encontrado"}, 404

        # Verificar se o novo CNPJ existe na tabela FORNECEDORES
        if novo_cnpj != None:
            fornecedor_existe = session.query(Fornecedores).filter_by(cnpj=novo_cnpj).first()
            if not fornecedor_existe:
                    return {"erro": "Fornecedor não encontrado"}, 400

        # Verificar se o novo código do produto existe na tabela PRODUTOS
        if novo_cod_produto != None:
            produto_existe = session.query(Produto).filter_by(cod_produto = int(novo_cod_produto)).first()
            if not produto_existe:
                return {"erro": "Produto não encontrado"}, 400

        # Atualizar os valores na tabela FORNECE
        if novo_cnpj != None:
            fornecimento.cnpj_fornecedor = novo_cnpj
        if novo_cod_produto != None:    
            fornecimento.cod_produto = int(novo_cod_produto)
        if nova_quantidade != None:
            fornecimento.quantidade = int(nova_quantidade)

        # Salvar as mudanças no banco
        session.commit()
        return {"mensagem": "Fornecimento atualizado com sucesso!"}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 500

    finally:
        session.close()


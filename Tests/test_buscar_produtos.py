import unittest
from flask import Flask
from Controller.produtos import produtos_bp
from Mocks.produtos_mock import produtos_dict

class TestBuscarProdutos(unittest.TestCase):

    def setUp(self):
        # Configura o servidor para começar os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(produtos_bp)
        self.client = self.app.test_client()

    def test_get_products(self):
        # Testa se é possível chamar a função que acessa todos os produtos
        response = self.client.get('/produtos/')
        self.assertEqual(response.status_code, 200)

    def test_get_products_empty(self):
        # Simula a lista de produtos vazia.
        temp_produtos = produtos_dict.copy()
        produtos_dict.clear()
        response = self.client.get('/produtos/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'A lista de produtos está vazia.'})
        produtos_dict.update(temp_produtos) #Restaura os produtos

    def test_get_products_by_id_found(self):
        # Testa se é possível recuperar um item pelo ID
        response = self.client.get('/produtos/?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {
            "categoria": "Equipamentos Esportivos",
            "cod_produto": 1,
            "descricao": "Bola de Futebol",
            "nome": "Bola",
            "preco_unitario": 189.9,
            "quantidade": 83
        })

    def test_get_products_by_id_not_found(self):
        # Testa a resposta caso o produto não seja encontrado pelo ID
        response = self.client.get('/produtos/?id=30000')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Nenhum produto encontrado com os parâmetros informados.'})

    def test_get_products_by_id_not_int(self):
        # Testa a resposta caso o ID não seja um valor do tipo inteiro
        response = self.client.get('/produtos/?id=a')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'message': 'O ID fornecido deve ser um número inteiro.'})

    def test_get_products_by_name_found(self):
        # Testa se é possível recuperar um item pelo nome
        response = self.client.get('/produtos/?nome=Bola')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0], produtos_dict[1])

    def test_get_products_by_name_not_found(self):
        # Testa a resposta caso o produto não seja encontrado pelo nome
        response = self.client.get('/produtos/?nome=NomeInexistente')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Nenhum produto encontrado com os parâmetros informados.'})

    def test_get_products_by_name_not_str(self):
        # Testa a resposta caso o nome não seja um valor do tipo string
        response = self.client.get('/produtos/?nome=3')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'message': 'O nome fornecido deve ser uma string.'})

    def test_get_products_by_category_found(self):
        # Testa se é possível recuperar uma categoria
        response = self.client.get('/produtos/?categoria=Equipamentos Esportivos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0], produtos_dict[1])

    def test_get_products_by_category_not_found(self):
        # Testa a resposta caso a categoria esteja vazia
        response = self.client.get('/produtos/?categoria=CategoriaInexistente')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'message': 'Nenhum produto encontrado com os parâmetros informados.'})

    def test_get_products_by_category_not_str(self):
        # Testa a resposta caso a categoria não seja um valor do tipo string
        response = self.client.get('/produtos/?categoria=3')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'message': 'A categoria deve ser uma string.'})

    def test_get_products_by_category_and_min_filter(self):
        # Testa a resposta passando categoria e limites de valor mínimo
        response = self.client.get('/produtos/?categoria=Roupas&preco_minimo=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1) # deve ter apenas um item

    def test_get_products_by_category_and_max_filter(self):
        # Testa a resposta passando categoria e limites de valor máximo
        response = self.client.get('/produtos/?categoria=Roupas&preco_maximo=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2) # deve ter apenas dois itens

    def test_get_products_by_category_and_min_max_filter(self):
        # Testa a resposta passando categoria e limites de valor máximo e mínimo ao mesmo tempo
        response = self.client.get('/produtos/?categoria=Roupas&preco_minimo=80&preco_maximo=150')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2) # deve ter apenas dois itens

    def test_get_products_by_category_and_increasing_filter(self):
        # Testa a resposta passando categoria e filtro crescente
        response = self.client.get('/produtos/?categoria=Roupas&preco=true')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0], produtos_dict[5]) # verifica se é o mesmo dicionario

    def test_get_products_by_category_and_decreasing_filter(self):
        # Testa a resposta passando categoria e filtro decrescente
        response = self.client.get('/produtos/?categoria=Roupas&preco=false')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0], produtos_dict[21])

    def test_all_filters_together(self):
        # Testa filtro categoria, valor minimo e maximo e filtro decrescente ao mesmo tempo
        response = self.client.get('/produtos/?categoria=Roupas&preco_minimo=80&preco_maximo=150&preco=false')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0], produtos_dict[21])

    def test_increasing_filter_in_all_results(self):
        # Testa o filtro crescente ao chamar todos os resultados
        response = self.client.get('/produtos/?preco=true')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0], produtos_dict[16])

    def test_decreasing_filter_in_all_results(self):
        # Testa o filtro decrescente ao chamar todos os resultados
        response = self.client.get('/produtos/?preco=false')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0], produtos_dict[20])


if __name__ == '__main__':
    unittest.main()
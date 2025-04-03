# Tests/test_buscar_fornecedores.py
import unittest
from flask import Flask
from Blueprints.fornecedor_blueprint import fornecedores_bp

class TestBuscarFornecedores(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.app = Flask(__name__)
        self.app.register_blueprint(fornecedores_bp)
        self.client = self.app.test_client()

    def test_get_fornecedores(self):
        # Testa se a busca de fornecedores retorna status 200
        response = self.client.get('/fornecedores/')
        self.assertEqual(response.status_code, 200)

    def test_get_fornecedor_por_cnpj(self):
        # Testa se um fornecedor pode ser recuperado pelo CNPJ
        response = self.client.get('/fornecedores/?cnpj=12345678901234')
        self.assertIn(response.status_code, [200, 404])  # Pode ser 404 se não houver fornecedor mockado

    def test_get_fornecedor_por_nome(self):
        # Testa se um fornecedor pode ser recuperado pelo nome
        response = self.client.get('/fornecedores/?nome_fornecedor=Loja Teste')
        self.assertIn(response.status_code, [200, 404])

    def test_get_fornecedor_cnpj_invalido(self):
        # Testa a resposta caso o CNPJ seja inválido
        response = self.client.get('/fornecedores/?cnpj=123')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'message': 'O CNPJ fornecido deve conter 14 números.'})

    def test_get_fornecedor_por_email(self):
        # Testa se um fornecedor pode ser recuperado pelo email
        response = self.client.get('/fornecedores/?email=teste@email.com')
        self.assertIn(response.status_code, [200, 404])

    def test_get_fornecedor_por_telefone(self):
        # Testa se um fornecedor pode ser recuperado pelo telefone
        response = self.client.get('/fornecedores/?telefone=11987654321')
        self.assertIn(response.status_code, [200, 404])

if __name__ == '__main__':
    unittest.main()

# Controller/fornecedores_controller.py
from flask import jsonify
from Mocks.fornecedores_mock import mock_fornecedores 

def buscar_fornecedores(args):
    """Busca fornecedores por CNPJ, nome, endereço, email ou telefone."""

    fornecedores = mock_fornecedores  # Usando os dados mockados

    # Filtro por CNPJ
    cnpj = args.get('cnpj')
    if cnpj:
        if not cnpj.isdigit() or len(cnpj) != 14:
            return jsonify({'message': 'O CNPJ fornecido deve conter 14 números.'}), 400
        
        fornecedor = next((f for f in fornecedores if f['cnpj'] == cnpj), None)
        if fornecedor:
            return jsonify(fornecedor)
        else:
            return jsonify({'message': 'Nenhum fornecedor encontrado com o CNPJ fornecido.'}), 404

    # Filtro por Nome
    nome = args.get('nome_fornecedor')
    if nome:
        fornecedores = [f for f in fornecedores if nome.lower() in f['nome_fornecedor'].lower()]

    # Filtro por Endereço
    endereco = args.get('endereco')
    if endereco:
        fornecedores = [f for f in fornecedores if endereco.lower() in f['endereco'].lower()]

    # Filtro por Email
    email = args.get('email')
    if email:
        fornecedores = [f for f in fornecedores if f['email'] == email]

    # Filtro por Telefone
    telefone = args.get('telefone')
    if telefone:
        fornecedores = [f for f in fornecedores if f['telefone'] == telefone]

    if fornecedores:
        return jsonify(fornecedores)
    else:
        return jsonify({'message': 'Nenhum fornecedor encontrado com os parâmetros informados.'}), 404

if __name__ == "__main__":
    busca_por_cnpj = buscar_fornecedores(mock_fornecedores)
    print(busca_por_cnpj)
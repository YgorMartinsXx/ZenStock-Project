from flask import Blueprint, request, jsonify
from Controller.usuario_controller import Buscar_usuario, criar_pedido, deleta_usuario, alterar_senha

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# Rota para buscar um usuário pelo login
@usuarios_bp.route('/<login_usuario>', methods=['GET'])
def get_usuario(login_usuario):
    return Buscar_usuario(login_usuario)

# Rota para criar um novo usuário
@usuarios_bp.route('/', methods=['POST'])
def post_usuario():
    data = request.get_json()
    login_usuario = data.get('login')
    senha = data.get('senha')
    cargo = data.get('cargo')
    
    if not login_usuario or not senha or not cargo:
        return jsonify({"erro": "Todos os campos são obrigatórios."}), 400
    
    return criar_pedido(login_usuario, senha, cargo)

# Rota para deletar um usuário pelo login
@usuarios_bp.route('/<login_usuario>', methods=['DELETE'])
def delete_usuario(login_usuario):
    return deleta_usuario(login_usuario)

# Rota para alterar a senha de um usuário
@usuarios_bp.route('/alterar_senha', methods=['PUT'])
def put_senha():
    data = request.get_json()
    login_usuario = data.get('login')
    nova_senha = data.get('nova_senha')
    
    if not login_usuario or not nova_senha:
        return jsonify({"erro": "Login e nova senha são obrigatórios."}), 400
    
    return alterar_senha(login_usuario, nova_senha)

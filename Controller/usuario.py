from flask import Blueprint, request, jsonify
from Repositories.usuario import GerenciadorUsuarios

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios_bp.route('/<login_usuario>', methods=['GET'])
def get_usuario(login_usuario):
    resposta, status = GerenciadorUsuarios.buscar_usuario(login_usuario)
    return jsonify(resposta), status

@usuarios_bp.route('/', methods=['POST'])
def post_usuario():
    data = request.get_json()
    login_usuario = data.get('login')
    senha = data.get('senha')
    cargo = data.get('cargo')

    if not login_usuario or not senha or not cargo:
        return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

    resposta, status = GerenciadorUsuarios.criar_usuario(login_usuario, senha, cargo)
    return jsonify(resposta), status

@usuarios_bp.route('/<login_usuario>', methods=['DELETE'])
def delete_usuario(login_usuario):
    resposta, status = GerenciadorUsuarios.deleta_usuario(login_usuario)
    return jsonify(resposta), status

@usuarios_bp.route('/alterar_senha', methods=['PUT'])
def put_senha():
    data = request.get_json()
    login_usuario = data.get('login')
    nova_senha = data.get('nova_senha')

    if not login_usuario or not nova_senha:
        return jsonify({"erro": "Login e nova senha são obrigatórios."}), 400

    resposta, status = GerenciadorUsuarios.alterar_senha(login_usuario, nova_senha)
    return jsonify(resposta), status

@usuarios_bp.route('/login', methods=['POST'])
def post_login():
    data = request.get_json()
    login = data.get('login')
    senha = data.get('senha')

    if not login or not senha:
        return jsonify({"erro": "Login e senha são obrigatórios."}), 400

    resposta, status = GerenciadorUsuarios.login_usuario(login, senha)
    return jsonify(resposta), status

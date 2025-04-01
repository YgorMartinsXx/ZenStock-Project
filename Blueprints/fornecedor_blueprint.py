from flask import Blueprint, request
from Controller.fornecedores_controller import buscar_fornecedores

fornecedores_bp = Blueprint('fornecedores', __name__, url_prefix='/fornecedores')

@fornecedores_bp.route('/', methods=['GET'])
def get_fornecedores():
    return buscar_fornecedores(request.args)

from flask import Blueprint, request
from Controller.produtos_controller import buscar_produtos

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

@produtos_bp.route('/', methods=['GET'])
def get_produtos():
    return buscar_produtos(request.args)
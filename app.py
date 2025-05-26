from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from Controller.produtos import produtos_bp
from Controller.fornece import fornecimento_bp
from Controller.pedido import pedidos_bp
from Controller.usuario import usuarios_bp
from Controller.fornecedores import fornecedores_bp
from Controller.movimentacoes import movimentacoes_bp

app = Flask(__name__)
CORS(app)

# Swagger
app.config['SWAGGER'] = {
    'title': 'API ZenStock',
    'uiversion': 3
}
Swagger(app)

# Blueprints
app.register_blueprint(produtos_bp)
app.register_blueprint(fornecimento_bp)
app.register_blueprint(pedidos_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(fornecedores_bp)
app.register_blueprint(movimentacoes_bp)


if __name__ == '__main__':
    app.run(debug=True)
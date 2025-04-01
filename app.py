from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from Blueprints.produtos_blueprint import produtos_bp
from Blueprints.fornece_blueprint import fornecimento_bp
from Blueprints.pedido_blueprint import pedidos_bp
from Blueprints.usuario_blueprint import usuarios_bp

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
app.register_blueprint(pedidos_bp) # nao identifiquei o erro ainda
app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    app.run(debug=True)
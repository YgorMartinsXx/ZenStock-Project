from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from Blueprints.produtos_blueprint import produtos_bp

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

if __name__ == '__main__':
    app.run(debug=True)
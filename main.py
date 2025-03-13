from flask import Flask
from Blueprints.produtos_blueprint import produtos_bp

app = Flask(__name__)

# Blueprints
app.register_blueprint(produtos_bp)

if __name__ == '__main__':
    app.run(debug=True) # debug=True apenas para desenvolvimento
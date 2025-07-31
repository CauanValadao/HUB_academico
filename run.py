# 1. Importações Iniciais
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# 2. Instanciação das Extensões (sem conectar ao app ainda)
db = SQLAlchemy()

# 3. A "Fábrica" de Aplicação
def create_app():
    # 4. Cria a instância principal do Flask
    app = Flask(__name__)
    
    # 5. Carrega as configurações do arquivo config.py
    app.config.from_object(Config)

    # 6. Conecta as extensões à instância do app
    db.init_app(app)

    # 7. Registra os Blueprints (rotas)
    from app.routes import api_bp
    app.register_blueprint(api_bp)

    # 8. Retorna o app configurado
    return app
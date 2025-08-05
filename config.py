import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Classe de configuração para a aplicação Flask.
    As variáveis de configuração são definidas como atributos da classe.
    """

    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_DATABASE = os.environ.get('DB_DATABASE')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')

    # 1. A String de Conexão com o Banco de Dados
    # A extensão Flask-SQLAlchemy pro cura por esta variável com este nome exato.
    # Use a URL que você já tinha, apenas ajuste o nome do banco se necessário.
    # URL = "mysql+mysqlconnector://<usuário>:<senha>@<host>/<nome_do_banco_de_dados>"
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'


    # 2. Configuração Opcional, mas Recomendada
    # Desativa o sistema de eventos do Flask-SQLAlchemy, que não usaremos e consome recursos.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
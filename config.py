import os

class Config:
    """
    Classe de configuração para a aplicação Flask.
    As variáveis de configuração são definidas como atributos da classe.
    """

    # 1. A String de Conexão com o Banco de Dados
    # A extensão Flask-SQLAlchemy procura por esta variável com este nome exato.
    # Use a URL que você já tinha, apenas ajuste o nome do banco se necessário.
    # URL = "mysql+mysqlconnector://<usuário>:<senha>@<host>/<nome_do_banco_de_dados>"
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{usuario}:{senha}@{host}/{nomeDoBancoDeDados}'


    # 2. Configuração Opcional, mas Recomendada
    # Desativa o sistema de eventos do Flask-SQLAlchemy, que não usaremos e consome recursos.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
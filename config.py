from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import contextmanager

DATABASE_URL = "mysql+mysqlconnector://root:3stUD4NT1!@localhost/hub-academico"
# Na URL tem a parte da senha, usuário, host e nome do banco de dados.
# Provavelmente você vai precisar alterar somente a senha para a sua e faça o nome do schema igual a hub-academico
# URL = "mysql+mysqlconnector://<usuário>:<senha>@<host>/<nome_do_banco_de_dados>"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine) 


# Classe que todas as tabelas criadas vão herdar
Base = declarative_base()

def create_tables():
    """
    Cria as tabelas no banco (se ainda não existirem).
    """
    # Importe os modelos aqui para garantir que sejam criados no banco de dados
    Base.metadata.create_all(bind=engine)

@contextmanager
def get_db():
    """
    Cria uma sessão de banco de dados para ser usada em cada requisição.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
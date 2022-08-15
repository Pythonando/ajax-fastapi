from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pessoa, Tokens
from secrets import token_hex
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


def conectaBanco():
    engine = create_engine("sqlite:///sqlite.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

app = FastAPI()



@app.post("/cadastro")
def cadastro(user: str, email: str, senha: str):
    if len(senha) < 6:
        return {'erro': 1}

    session = conectaBanco()
    usuario = session.query(Pessoa).filter_by(email=email, senha=senha).all()

    if len(usuario) > 0:
        return {'erro': 2}

    try:
        novo_usuario = Pessoa(
            usuario = user,
            email = email,
            senha = senha
        )

        session.add(novo_usuario)
        session.commit()
        return {'erro': 0}
    except Exception as e:
        return {'erro': 3, 'erro': e}

if __name__ == "__main__":
    uvicorn.run('controller:app', port=5000, reload=True, access_log=False)
    
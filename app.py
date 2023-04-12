from fastapi import FastAPI
import json
import main

app = FastAPI()


@app.get("/")
def home():
    string = "Bem vindo ao gerador de senha! Para gerar uma senha basta chamar /password?length=? e passar no lugar da interrogacao a quantidade de caracteres que voce quer Caso tenha ficado alguma duvida basta chamar /docs"
    return string


@app.get("/password")
async def generate_password(length: int):
    # Seu código de geração de senha aqui
    return {"password": main.generated_password(length)}

from fastapi import FastAPI, Body
import json

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint para exibir a mensagem mais famosa da programaçao
    '''
    return {'hello':'world'}   

@app.get('/api/sayhi/{nome}')
def say_hi(nome:str):
    return {'Oi': nome} 

@app.get('/api/bandas')
def exibir_bandas():
    '''Endpoint para listar todas as bandas do "banco de dados"'''
    with open('data.json', 'r') as file:
        dados = json.load(file)
    return dados

@app.post('/api/bandas')
def adicionar_nova_banda(banda: dict = Body):
    with open('data.json', 'r') as file:
        dados = json.load(file)
    dados.append(banda)
    with open('data.json', 'w') as file:
        json.dump(dados, file)
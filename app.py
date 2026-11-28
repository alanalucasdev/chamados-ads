from flask import Flask, request

app = Flask(__name__)

'''
VARIÁVEIS PARA SALVAR OS DADOS - TEMPORÁRIO
'''
chamados = []
proximo_id = 1

'''
Rotas da aplicação
'''

@app.get("/")
def inicio():
    ''' Rota inicial da aplicação'''
    return {
        "mensagem": "API de chamados em funcionamento"
    }

@app.post("/chamados")
def create_chamado():
    ''' Salva o chamado'''
    global chamados
    global proximo_id

    chamado = request.json

    # Adiciona um id ao chamado
    chamado["id"] = proximo_id


    chamado["status"] = "aberto"

     # Adiciona um novo chamado à nossa lista de chamados
    chamados.append(chamado)

    # Incrementa o próximo id
    proximo_id += 1
    
    return chamado, 201

@app.get("/chamados")
def get_chamados():
    ''' Rota para obter todos os chamados'''
    global chamados
    return chamados

@app.get("/chamados/<int:chamado_id>")
def get_chamado_by_id(chamado_id):
    ''' Retorna o chamado que tem id == chamado_id '''
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado, 200
        
    return {"mensagem": "Chamado não encontrado"}, 404 

if __name__ == "__main__":
    app.run(debug=True)
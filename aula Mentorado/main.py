from fastapi import FastAPI

app = FastAPI()


vendas = {
    1:{"item": "lata", "preço-unitario": 4, "quantidade": 5},
    2:{"item": "garrafa 2L", "preço-unitario": 15, "quantidade": 5},
    3:{"item": "garrafa 750ml", "preço-unitario": 10, "quantidade": 5},
    4:{"item": "lata mini", "preço-unitario": 2, "quantidade": 5},
}

@app.get("/")
def home():
    return {"vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_vendas(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "ID venda inexistente"}
import json

arquivo = open("ex1.txt", mode="r", encoding="utf8")

dado = json.load(arquivo)
print(dado)
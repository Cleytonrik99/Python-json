import json

# lista = [

#     familia1 := {
#         'pai': {'nome': 'Roberto', 'idade': 50},
#         'mae': {'nome': 'Marta', 'idade': 48}
#     },

#     familia2 := {
#         'mae': {'nome': 'Julia', 'idade': 22},
#         'mae': {'nome': 'Leticia', 'idade': 19}
#     }
# ]

lista = [
    dados_cliente := {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
    },

    dados_cliente2 := {
    'Nome': 'Augusto',
    'Endereco': 'Rua Capote Valente',
    'Telefone': '912345678'
    }
]

arquivo = open("ex1.txt", mode="w", encoding="utf8")
json.dump(lista, arquivo, indent=4)
arquivo.close()

print("Programa Finalizado")


import json

def menu():
    print("1) cadastra")
    print("2) consulta")
    print("3) sair")
    opcao = int(input("Opcao: "))
    return opcao

def leitura_arquivo():
    print("Lendo arquivo")

def cadastro(info: dict):
    print("cadastrando info PIX")

def consulta(dados) -> object:
    print("Fazendo a consulta")
    return None

def gravacao_arquivo(info: dict):
    print("Gravando arquivos")

if __name__ == "__main__":
    print("SISTEMA CHAVE PIX")
    escolha = menu()

    dados = leitura_arquivo()

    while escolha != 3:
        if escolha == 1:
            cadastro(dados)
        elif escolha == 2:
            resultados = consulta(dados)
            print(resultados)
        elif escolha != 3:
            print("Opção inválida!")
        
        escolha = menu()

    gravacao_arquivo(dados)
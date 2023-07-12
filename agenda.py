import os

def print_menu():
    print("-----------------------------------------")
    print("---- MENU DE OPÇÕES ---------------------")
    print("---- 1 = Adicionar contato --------------")
    print("---- 2 = Listar contatos ----------------")
    print("---- 3 = Procurar contato ---------------")
    print("---- 4 = Editar contato -----------------")
    print("---- 5 = Excluir contato ----------------")
    print("---- 6 = Limpar lista de contatos -------")
    print("---- 7 = Numero de contatos -------------")
    print("---- 8 = Sair ---------------------------\n")

    try:
        return int(input("Digite o numero da opção desejada: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return 0

def salvar_agenda(agenda):
    arquivo = open("agenda.txt", "w")

    for contato in agenda:
        arquivo.write(f"{contato['nome']},{contato['telefone']}\n")

    arquivo.close()

def carregar_agenda():
    # Verificar se o arquivo agenda existe, caso não exista criar um novo
    if not os.path.exists("agenda.txt"):
        salvar_agenda([]) # Usar a função de salvar para criar um novo aqui com a agenda zerada usando []

    # Carregar dados do arquivo
    arquivo = open("agenda.txt", "r")
    contatos = arquivo.readlines()
    arquivo.close()

    # Criar uma agenda na memoria
    agenda = [] # Definir lista
    for contato in contatos:
        nome, telefone = contato.strip().split(',')
        agenda.append({"nome":nome, "telefone":telefone})

    return agenda

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input ("Digite o numero do contato: ")
    agenda.append({"nome":nome, "telefone":telefone})

    salvar_agenda(agenda) # Salvar lista no arquivo
    print("Contato inserido com sucesso!")

def listar_contatos(agenda):
    print("---- Lista de contatos ------------")
    for contato in agenda:
        print(f" - {contato['nome']}: {contato['telefone']}")

def procurar_contato(agenda):
    encontrados = [] #Definir lista de contatos encontrados

    # pedir o nome ou o telefone que deseja procurar
    palavra_chave = input("Digite o nome ou telefone que deseja encontrar: ")

    # procurar por nome
    for contato in agenda:
        if contato["nome"] == palavra_chave:
            encontrados.append(contato)

    # verificar se achou um contato, se não procurar por telefone
    if (len(encontrados) <= 0):
        for contato in agenda:
            if contato["telefone"] == palavra_chave:
                encontrados.append(contato)

    # verificar novamente se não encontrou nenhum contato
    if (len(encontrados) > 0):
        print(f"- {len(encontrados)} contato(s) encontrado(s)!")
        for contato in encontrados:
            print(f"- {contato['nome']}: {contato['telefone']}")
    else:
        print("Nenhum contato encontrado!")
        
def main():
    print("-- Bem vindo a agenda 2.0 --")

    print("Carregando contatos...")
    agenda = carregar_agenda()

    while(True):
        op = print_menu()

        if op == 1:
            adicionar_contato(agenda)
        elif op == 2:
            listar_contatos(agenda)
        elif op == 3:
            procurar_contato(agenda)
        elif op == 8:
            break
        else:
            print("Opção inválida, tente novamente!")

# Verificar se o arquivo está sendo executado como um programa
if __name__ == "__main__":
    main()

    
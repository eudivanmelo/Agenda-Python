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

def editar_contato(agenda):
    encontrados = [] #Definir lista de contatos encontrados

    # pedir o nome ou o telefone que deseja editar
    palavra_chave = input("Digite o nome do contato que deseja editar: ")

    # procurar por nome
    for contato in agenda:
        if contato["nome"] == palavra_chave:
            encontrados.append(agenda.index(contato))

    if (len(encontrados) > 1):
        print("Foi encontrado mais de um contato!")
        for index in range(len(encontrados)):
            print(f"{index}: {agenda[encontrados[index]]['nome']} - {agenda[encontrados[index]]['telefone']}")

        id = int(input("Digite o numero correspondente a id do contato que deseja editar: "))
        if id < 0 and id >= len(encontrados):
            print("Id inválida, tente novamente!")
            return
        else:
            id = encontrados[id]

    elif (len(encontrados) == 1):
        id = encontrados[0]

    else:
        print("Nenhum contato encontrato!")
        return

    nome = input(f"Digite o novo nome para {agenda[id]['nome']}:")
    if len(nome) > 0:
        agenda[id]['nome'] = nome

    
    telefone = input(f"Digite o novo telefone para {agenda[id]['nome']}:")
    if len(telefone) > 0:
        agenda[id]['telefone'] = telefone

    salvar_agenda(agenda)
    print("Contato alterado com sucesso!")

def excluir_contato(agenda):
    encontrados = [] #Definir lista de contatos encontrados

    # pedir o nome ou o telefone que deseja editar
    palavra_chave = input("Digite o nome do contato que deseja excluir: ")

    # procurar por nome
    for contato in agenda:
        if contato["nome"] == palavra_chave:
            encontrados.append(agenda.index(contato))

    if (len(encontrados) > 1):
        print("Foi encontrado mais de um contato!")
        for index in range(len(encontrados)):
            print(f"{index}: {agenda[encontrados[index]]['nome']} - {agenda[encontrados[index]]['telefone']}")

        id = int(input("Digite o numero correspondente a id do contato que deseja excluir: "))
        if id < 0 and id >= len(encontrados):
            print("Id inválida, tente novamente!")
            return
        else:
            id = encontrados[id]

    elif (len(encontrados) == 1):
        id = encontrados[0]

    else:
        print("Nenhum contato encontrato!")
        return

    confirm = input(f"Tem certeza que deseja excluir {agenda[id]['nome']} da lista de contatos (s/n)?: ")
    if confirm == "s" or confirm == "S":
        agenda.pop(id)
        salvar_agenda(agenda)
        print("Contato excluido com sucesso!")
        
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

        elif op == 4:
            editar_contato(agenda)

        elif op == 5:
            excluir_contato(agenda)

        elif op == 6:
            confirm = input(f"Tem certeza que deseja excluir a lista de contatos (s/n)?: ")
            if confirm == "s" or confirm == "S":
                agenda.clear()
                salvar_agenda(agenda)
                print("Agenda excluida com sucesso!")
        elif op == 7:
            print(f"A agenda tem {len(agenda)} contatos cadastrados!\n")
        elif op == 8:
            break
        else:
            print("Opção inválida, tente novamente!")

# Verificar se o arquivo está sendo executado como um programa
if __name__ == "__main__":
    main()

    
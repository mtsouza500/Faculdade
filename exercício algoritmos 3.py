#Adicionar Cliente

clientes = []
def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)


#Exibir Cliente

def exibir_cliente():
    for cliente in clientes:
        print(f"Nome: {cliente[0]} ")
        print(f"Email: {cliente[1]}")
        print(f"Telefone: {cliente[2]}")
        print(f"Endereço: {cliente[3]}")


#Buscar Cliente por email

def buscar_cliente(email):
    cliente_encontrado = False

    for cliente in clientes:
        if cliente[1] == email:
            print(f"Nome: {cliente[0]}, Email: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")
            cliente_encontrado = True
            break
    
    if not cliente_encontrado:
        print("Cliente não encontrado.")
         


#Remover Cliente

def remover_cliente(email):
    cliente_encontrado = False
    for i, cliente in enumerate(clientes):
        if cliente[1] == email:
            del clientes[i]
            print("Cliente removido com sucesso.")
            cliente_encontrado = True
            break

    if not cliente_encontrado:
        print("Cliente não encontrado.")

#Teste de funcionalidade

while True:
    print("Escolha uma opção:")
    print("1. Adicionar cliente")
    print("2. Exibir clientes")
    print("3. Buscar cliente")
    print("4. Remover cliente")
    print("5. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        adicionar_cliente(nome, email, telefone, endereco)
    elif opcao == "2":
        if clientes:
            exibir_cliente()
        else:
            print("Nenhum cliente foi cadastrado.Faça um cadastro")
    elif opcao == "3":
        email = input("Digite o email do cliente: ")
        buscar_cliente(email)
    elif opcao == "4":
        email = input("Digite o email do cliente: ")
        remover_cliente(email)
    elif opcao == "5":
        break
    else:
        print("Opção inválida.")
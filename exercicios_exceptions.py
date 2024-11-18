#Exercício 1 - Exceções básicas: 

try:
    num1 = int(input('Insira o primeiro número: '))
    num2 = int(input('Insira o segundo número: '))
    div = int(num1 / num2)
    print(f'A divisão é: {div}')

except ZeroDivisionError:
    print('Erro: Divisão por zero não pode ser feito.')
except ValueError:
    print('Erro: Não permite o uso de letras, apenas números inteiros.')

#Exercício 2 - Exceções multiplas: 

try: 
    cores = {'vermelho': (255, 0, 0), 
             'verde': (0, 255, 0), 
             'azul': (0, 0, 255)}
    
    cor = input('Insira a cor desejada (vermelho, verde ou azul): ')
    rgb = cores[cor]
    print(f'A cor selecionada foi {cor} e o rgb dela é {rgb}')

except KeyError:
    print('Erro: Cor inválida. Use vermelho, verde ou azul.')

#Exercício 3 - Bloco else e finally:

try: 
    numero = int(input('Insira um número: '))
    if numero > 10:
        print('É um número válido.')
    else:
        print('Programa executado com sucesso!')
finally:
    print('Programa finalizado!')
    
#Exercício 4 - Exceções personalizadas:

try:
    def senha_grande():
        senha = input('Insira a sua senha: ')
        if len(senha) < 8:
            raise ValueError('Senha muito pequena. Ela deve conter mais de 8 caracteres.')
        if not any(char.isdigit() for char in senha):
            raise ValueError('Senha sem números. A senha tem que conter um número.')
        else:
            print('Senha válida!')

    senha_grande()
    
finally:
    print('Programa finalizado!')

#Exercício 5 - Simulação  de transações: 

try:
    saldo = 500
    conta_vazia = ()
    while True:
        print('1. Consulta saldo\n2. Transferir')
        opcao = int(input('Escolha uma ação que deseja: '))
        
        if opcao == 1:
            print(f'Seu saldo é de: {saldo}')
        elif opcao == 2:
            conta2 = input('Insira o número da conta que deseja transferir: ')
            transferencia = int(input('Digite o valor que deseja transferir: '))
            if transferencia > saldo:
                print('Saldo insuficiente.')
                continue
            if conta2 not in conta_vazia:
                saldo -= transferencia
                print(f'Transferência realizada com sucesso. Saldo atual: {saldo}')
            if saldo == 0:
                print('Sua conta foi encerrada. Saldo esgotado')
                break
        else:
            print('Opção incorreta. Tente novamente!')
            continue
   


except ValueError as e:
    print(f'Erro: {e}')



    
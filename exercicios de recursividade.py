"""

1 - Implemente uma função recursiva que calcule a potência de um número (base^expoente).

"""

def potencia_recursiva(b, e):
    if e == 0:
        return 1
    else:
        return b * potencia_recursiva(b, e-1)

# Execução da função

resultado = potencia_recursiva(2, 3)
print(f"Resposta do exercício 1 é:\n O resultado da potência é {resultado}\n")


"""

2 - Crie uma função recursiva para calcular o n-ésimo termo da sequência de 
Fibonacci.Lembre-se de que a sequência começa com 0 e 1.

"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Execução da função

n = 10
termo_fibonacci = fibonacci(n)
print(f"\nResposta do exercício 2 é: \n O {n}-ésimo termo da sequência de Fibonacci é {termo_fibonacci}\n")


"""

3 - Escreva uma função recursiva que conte quantos dígitos um número tem.

"""

def contar_digitos(n_digitos):
    if n_digitos == 0:
        return 0
    else:
        return 1 + contar_digitos(n_digitos // 10)

# Execução da função

n_digitos = 1998
digitos = contar_digitos(n_digitos)
print(f"\nResposta do exercício 3 é: \n O número {n_digitos} tem {digitos} dígitos\n")


"""

4 - Escreva uma função recursiva que verifique se uma string é um palíndromo.

"""

def verifica_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    else:
        return palavra[0] == palavra[-1] and verifica_palindromo(palavra[1:-1])

# Execução da função

palavra = "1001"
palindromo = verifica_palindromo(palavra)
print(f"\nResposta do exercício 4 é: \n A palavra '{palavra}' {'é' if palindromo else 'não é'} um palíndromo\n")








#-----------LISTAS-------------

#Exercicio - 1

import random

def criacao_lista():
    lista = [random.randint(1, 100) for i in range(10)]
    print(f"A lista é:{lista}\nO maior e o menor número é", max(lista),"\nE o Menor número:", min(lista))

criacao_lista()

#Exercicio - 2

def acessar_fruta():
    lista_fruta = []
    for i in range(5):
        lista_fruta.append(input("Insira o nome de uma fruta: "))
    fruta = input("Insira o nome da fruta para saber se ela está na lista:")
    if fruta in lista_fruta:
        print(f"{fruta} está na lista.")
    else:
        print(f"A fruta{fruta} não está na listagem")
    

acessar_fruta()

#Exercicio - 3

def calculo_media():
    numeros = []
    while True:
        for i in range(10):
            numeros.append(int(input("Insira um valor: ")))
        media = sum(numeros)/ len(numeros)
        print(f"A média dos valores é: {media:.2f}")
        break
    
        
calculo_media()

#Exercicio - 4

lista_pessoas = [["Matheus Souza", 26, "Saquarema"], ["Matheus Silva", 19, "Madri"], ["Motta", 26, "Araruama"]]

for pessoa in lista_pessoas:
    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Cidade: {pessoa[2]}")

#Exercicio - 5

lista = []

while True:
    for i in range(5):
        lista.append(int(input("Insira um valor: ")))
        lista = list(dict.fromkeys(lista))
        lista.sort(reverse=False)
        print(lista)
    break


#-----------DICIONÁRIO-------------

#Exercicio - 6

dicionario_semanal = {
    "Segunda": 0,
    "Terça": 0,
    "Quarta": 0,
    "Quinta": 0,
    "Sexta": 0,
}
dicionario_semanal["Segunda"] = int(input("Horas trabalhadas de Segunda: "))
dicionario_semanal["Terça"] = int(input("Horas trabalhadas de Terça: "))
dicionario_semanal["Quarta"] = int(input("Horas trabalhadas de Quarta: "))
dicionario_semanal["Quinta"] = int(input("Horas trabalhadas de Quinta: "))
dicionario_semanal["Sexta"] = int(input("Horas trabalhadas de Sexta: "))

soma_horas = (sum(dicionario_semanal.values()))

print(f"A escala de horas semanais é assim: {dicionario_semanal}\nHoras trabalhadas totais da semana é: {soma_horas}")

#Exercicio - 7

alunos = ["Matheus Souza", "Matheus Silva", "Motta"]
notas = [90,95,80]
alunos_notas = dict(zip(alunos, notas))
alunos_notas.update({input("Insira o nome do aluno: "): int(input("Insira a nota do aluno: "))})
print(alunos_notas)

#Exercicio - 8

estoque = {
    'bola':10,
    'camisa':5,
    'chinelo':20,
    'chuteira':60,
    'shorts':15,
    'apito':0
}

def verifica_estoque(produto):
    if estoque[produto] > 0:
        print(f'O produto {produto} está em estoque. Quantidade: {estoque[produto]}')
    else: 
        print(f'O produto {produto} não está em estoque.')
    
verifica = input('Insira o nome do produto: ')
verifica_estoque(verifica)

#Exercicio - 9

nomes_paises = ['Brasil','Estados Unidos','França','Inglaterra']
paises_capitais = ['Brasília','Washington D.C','Paris','Londres']
dic_paises = dict(zip(nomes_paises, paises_capitais))
print(dic_paises)

#Exercicio - 10

dic_estudantes = {
    'Matheus Souza': {'Matemática': 90, 'Português': 85, 'Ciências': 80},
    'Matheus Silva': {'Matemática': 85, 'Português': 90, 'Ciências': 75},
    'Motta': {'Matemática': 95, 'Português': 90, 'Ciências': 85}
}

aluno = input("Insira o nome do estudante: ")
disciplinas = input("Insira o nome da disciplina: ")
notas = input("Insira a nota para atualizar: ")

if aluno in dic_estudantes:
    if disciplinas in dic_estudantes[aluno]:
        dic_estudantes[aluno][disciplinas] = int(notas)
    else:
        print("Disciplina não encontrada.")

print(dic_estudantes)


#-----------FUNÇÕES-------------

#Exercicio - 11

def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = soma_pares(lista)
print(resultado)

#Exercicio - 12

def mais_caro(dicionario):
    produto = ''
    preco = 0
    for chave, valor in dicionario.items():
        if valor > preco:
            produto = chave
            preco = valor
    return produto

dicionario = {
    'Notebook Asus AMD Ryzen 4600, RTX 3050': 3599.99,
    'Mouse Death Adder - Razer': 149.99,
    'Teclado Logitech': 259.99,
    'RTX 4060 - 8gb': 1799.99,
    'SSD Kingston A400 NVMe 1TB': 329.99
}

caro = mais_caro(dicionario)
print(caro)

#Exercicio - 13

lista = [1,2,3,4,5,6,7,8,9,10]

def multi(lista, n = input('Informe um numero para multiplicar: ')):
    novalista=[]
    if n == '':
        n=1
    else:
        n = int(n)
    
    for i, valor in enumerate(lista):
        novalista.append(valor * n)
    return novalista

resultado = multi(lista)
print(resultado)

#Exercicio - 14

def modifica(estoque, venda):
    if venda['nome'] in estoque and estoque[venda['nome']] >= venda['quantidade']:
        estoque[venda['nome']] -= venda['quantidade']
        return f"Venda realizada com sucesso. O estoque de {venda['nome']} agora é {estoque[venda['nome']]}."
    else:
        return "Venda não realizada. Quantidade vendida excede o estoque disponível."

estoque = {
    'banana': 14, 
    'maçã': 5, 
    'uva': 7,
    'laranja': 12, 
    'pera': 21,
    'mamão': 18,
}

venda = {
    'nome': 'banana',
    'quantidade': 4,
}

print(modifica(estoque, venda))

#Exercicio - 15

def calcula_media_estudantes(estudantes):
    medias = {}
    for estudante in estudantes:
        media = sum(estudante['notas']) / len(estudante['notas'])
        medias[estudante['nome']] = media
    return medias
estudantes = [
    {'nome': 'Matheus Souza', 'notas': [90, 85, 95]},
    {'nome': 'Matheus Silva', 'notas': [80, 75, 85]},
    {'nome': 'Jonatas Motta', 'notas': [95, 90, 88]},
]

media_estudantes = calcula_media_estudantes(estudantes)
print(media_estudantes)

#Exercicio - 16

def busca_binaria(lista, chave, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio > fim:
        return None
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == chave:
        return meio, chave
    elif lista[meio] < chave:
        return busca_binaria(lista, chave, meio + 1, fim)
    elif lista[meio] > chave:
        return busca_binaria(lista, chave, inicio, meio - 1)

        
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
chave = 7
posicao, valor = busca_binaria(numeros, chave)
print(f"Lista ordenada: {sorted(numeros)}")
print(f"O número {chave} está na posição {posicao} e seu valor é {valor}.")

##Tarefa de Implementação

livros = []

def cadastrar_livro(titulo, autor, genero, quantidade,codigo):
    cadastro = {
        'título': titulo,
        'autor': autor,
        'gênero': genero,
        'quantidade': quantidade,
        'código': codigo
    }
    livros.append(cadastro)
    print(f"Livro {titulo} foi cadastrado.")

def busca_livro(codigo):
    livro_encontrado = False
    for cadastro in livros:
        if cadastro["código"] == codigo:
            print(f"título: {cadastro['título']}\n"
              f"autor: {cadastro['autor']}\n"
              f"gênero: {cadastro['gênero']}\n"
              f"quantidade: {cadastro['quantidade']}\n"
              f"código: {cadastro['código']}\n"
              )
            livro_encontrado = True
            break
    if not livro_encontrado:
        print("Livro não encontrado")

def atualizar_estoque(codigo, nova_quantidade):
    for cadastro in livros:
        if cadastro["código"] == codigo:
            cadastro["quantidade"] == nova_quantidade
            print(f'O livro do {codigo} agora tem o estoque de {nova_quantidade} livros.')
            return
        
def remover_livro(codigo):
    livro_encontrado = False
    for cadastro in livros:
        if cadastro["código"] == codigo:
            del cadastro["código"]
            print("Livro removido!")
            livro_encontrado = True
            break
    
    if not livro_encontrado:
        print("Livro não encontrado")

def listar_livros():
    if not livros:
        print("Não há livros cadastrados.")
        return
    for cadastro in livros:
        print(f"título:{cadastro['título']}\n"
              f"autor:{cadastro['autor']}\n"
              f"gênero:{cadastro['gênero']}\n"
              f"quantidade:{cadastro['quantidade']}\n"
              f"código:{cadastro['código']}\n"
              )
        
cadastrar_livro("As tranças do careca", "Silva Theus","Comédia", 300, "AK47-762")
cadastrar_livro("A volta dos que não foram", "Silva Theus e Souza Thue","Comédia", 777, "002200")
cadastrar_livro("Piratas do Caribe Navegadando por Cumes Misteriosos", "Jonatas Motta","Comédia", 24, "Amem")
print("\n")
print("-"*25)
print("\n")
busca_livro("Amem")
print("\n")
print("-"*25)
print("\n")
remover_livro("002200")
print("\n")
print("-"*25)
print("\n")
listar_livros()

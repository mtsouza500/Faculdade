
import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

b_inicio_tempo = time.time()
lista_bubble = [random.randint(1, 10000000) for contagem in range(10000000)]
fim_do_tempo = time.time()
bubblesort_tempo = fim_do_tempo - b_inicio_tempo

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        index_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[index_minimo]:
                index_minimo = j
        lista[i], lista[index_minimo] = lista[index_minimo], lista[i]
    return lista

s_inicio_tempo = time.time()
lista_selection = [random.randint(1, 10000000) for contagem in range(10000000)]
fim_tempo = time.time()
selection_tempo = fim_tempo - s_inicio_tempo

print("-"*50)
print(f"Para o bubble sort ordenar 10kk de números sorteados\nEle leva aproximadamente: {bubblesort_tempo} segundos")
print("-"*50)
print(f"Para o selection sort ordenar 10kk de números sorteados\nEle leva aproximadamente: {selection_tempo} segundos")
print("-"*50)



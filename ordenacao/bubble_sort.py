'''
Implementação do Bubble Sort em Python3
'''

def bubble_sort(lista):
    ordenado = False #Assumimos que a lista não está ordenada
    while not ordenado:
        ordenado = True #Assumimos a possibilidade da lista já estar ordenada
        for i in range(len(lista)-1): #Iterando sobre a lista
            if lista[i] > lista[i+1]: #Se o elemento à direita for maior que o à esquerda...
                lista[i], lista[i+1] = lista[i+1], lista[i] #Troca de posição
                ordenado = False #Assumimos uma desordenação na lista


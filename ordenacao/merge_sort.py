'''
Implementação do Merge Sort em Python3
'''

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio] #Lado esquerdo da lista
    direita = lista[meio:fim] #Lado direito da lista
    e = 0 #Topo do lado esquerdo
    d = 0 #Topo do lado direito
    for i in range(inicio, fim): #Iterando do inicio ao fim da lista
        if e >= len(esquerda): #Se o topo da esquerda for maior que a lista da esquerda...
            lista[i] = direita[d] #O topo da direita é adicionado à posição i da lista
            d += 1 #Incrementa o topo da direita
        elif d >= len(direita): #Se o topo da direita for maior que a lista da direita...
            lista[i] = esquerda[e] #O topo da esquerda é adicionado à posição i da lista
            e += 1 #Incrementa o topo da esqueda
        elif esquerda[e] < direita[d]: #Se o topo da esquerda é menor que o da direita...
            lista[i] = esquerda[e] #O topo da esquerda é adicionado à posição i da lista
            e += 1 #Incrementa o topo da esqueda
        else: #Caso nada anterior acontecer, então o topo da direita é menor...
            lista[i] = direita[d] #O topop da direita é adicionado à posição i da lista
            d += 1 #Incrementa o topo da direita


def merge_sort(lista, inicio=0, fim=None):
    #Se o parâmetro fim for None, então consideramos o fim como sendo o tamanho da lista, isto é, estamos na primeira chamada do merge_sort
    if fim == None:
        fim = len(lista)
    
    #Se o fim for maior que o início, ou seja, se a lista é válida...
    if fim - inicio > 1:
        meio = (fim + inicio) // 2 #Fazemos a mediana da lista para descobrir a posição do meio
        merge_sort(lista, inicio, meio) #Ordenamos a primeira metade
        merge_sort(lista, meio, fim) #Ordenamos a segunda metade
        merge(lista, inicio, meio, fim) #Juntamos as partes


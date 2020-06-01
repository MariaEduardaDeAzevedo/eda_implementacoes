'''
Implementação do Insertion Sort em Python3
'''

def insertion_sort(lista):
    for i in range(1, len(lista)): #Iterando a lista partindo do 2° elemento
        atual = i #Posição atual
        anterior = i - 1 #Posição anterior
        #Enquanto houver um elemento anterior e o elemento atual for menor que o anterior...
        while anterior >= 0 and lista[atual] < lista[anterior]: 
            lista[atual], lista[anterior] = lista[anterior], lista[atual] #Trocamos as posições
            atual -= 1; #Decrementa a posição atual
            anterior -= 1; #Decrementa a posição anterior

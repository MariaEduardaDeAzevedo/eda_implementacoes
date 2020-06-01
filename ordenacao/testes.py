from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

def test_bubble_sort():
    bubble_sort(lista_0)
    bubble_sort(lista_1)
    bubble_sort(lista_2)
    bubble_sort(lista_3)
    bubble_sort(lista_4)
    bubble_sort(lista_5)
    bubble_sort(lista_6)

def test_selection_sort():
    selection_sort(lista_0)
    selection_sort(lista_1)
    selection_sort(lista_2)
    selection_sort(lista_3)
    selection_sort(lista_4)
    selection_sort(lista_5)
    selection_sort(lista_6)

def test_insertion_sort():
    insertion_sort(lista_0)
    insertion_sort(lista_1)
    insertion_sort(lista_2)
    insertion_sort(lista_3)
    insertion_sort(lista_4)
    insertion_sort(lista_5)
    insertion_sort(lista_6)

def test_merge_sort():
    merge_sort(lista_0)
    merge_sort(lista_1)
    merge_sort(lista_2)
    merge_sort(lista_3)
    merge_sort(lista_4)
    merge_sort(lista_5)
    merge_sort(lista_6)

# -------------------- Casos de teste -----------------------

lista_0 = [] #Lista vazia
lista_1 = [1] #Lista com um elemento
lista_2 = [1, 2] #Lista com dois elementos ordenados
lista_3 = [2, 1] #Lista com dois elementos não ordenados
lista_4 = [1, 2, 3, 4, 5] #Lista ordenada
lista_5 = [5, 4, 3, 2, 1] #Lista ordenada de forma decrescente
lista_6 = [2, 5, 1, 3, 4] #Lista totalmente desordenada

#test_bubble_sort()
#test_selection_sort()
#test_insertion_sort()
#test_merge_sort()

assert lista_0 == []
assert lista_1 == [1]
assert lista_2 == [1, 2]
assert lista_3 == [1, 2]
assert lista_4 == [1, 2, 3, 4, 5]
assert lista_5 == [1, 2, 3, 4, 5]
assert lista_6 == [1, 2, 3, 4, 5]
print("Passou nos testes")

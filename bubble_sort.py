def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1): 
        for j in range(n - i - 1):  
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [5, 3, 8, 2, 1]

print("Lista original:", numeros)

ordenada = bubble_sort(numeros)

print("Lista ordenada:", ordenada)

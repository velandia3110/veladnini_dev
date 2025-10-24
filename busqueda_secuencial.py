def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  
    return -1  

numeros = [3, 7, 1, 9, 5]
pos = busqueda_lineal(numeros, 9)
print("Encontrado en la posición:", pos)

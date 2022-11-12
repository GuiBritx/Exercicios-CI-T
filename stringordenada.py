def string_ordenada(idk):
    lista = []
    idk.sort()
    n = len(idk)
    for i in range(int(n)):
        print("lista :", lista)
        lista.append(idk[-1])
        print(idk)
        idk = idk[:-1]
        idk.reverse()
    return lista

def string_ordenada2(idk):
    lista = []
    idk.sort()
    lista2 = idk
    n = len(lista2)
    for i in range(int(n/2)):
        lista.append(lista2[-1])
        lista.append(lista2[0])
        lista2 = lista2[1:-1]
    if n % 2 != 0:
        lista.append(idk[int(n/2)])
    return lista
lista = [2, 10, 4, 6, 8, 12, 16]
print(lista)
nlista = string_ordenada(lista)
nlista2 = string_ordenada2(lista)
print(nlista)
print(nlista2)


def fat(x):
    lista = []

    if (len(lista)) == 0:
        for i in range(2, 10000):
            if (x % i) == 0:
                lista.append(i)
    
    return lista



print(fat(5689))


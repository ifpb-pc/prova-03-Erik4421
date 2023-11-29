def q1(cidades):
    x = list(cidades.items())
    resultado = []
    for i in x:
        if i[1] > 100:
            resultado.append(i[0])
    return resultado

def q2(lista1, lista2):
    
    lista = []

    for i in range(len(lista1)):
        if lista1[i] > 0:
            lista.append(lista1[i])
        if lista2[i] > 0:
            lista.append(lista2[i])
    soma = sum(lista)
    lista.sort()
    return (soma, lista)

    

def q3():
    
    num = None
    valores = []
    while num != 0:
        num = int(input('Digite (pare digitando 0): '))
        valores.append(num)


    par = []
    impar = []

    for i in valores:
        if i % 2 == 0 and i != 0:
            par.append(i)
        elif i % 2 != 0 and i != 0:
            impar.append(i)
    return print([par],[impar])

def q4():
    pass
        


def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    main()





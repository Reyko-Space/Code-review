def fibonacci(n):
    i = 0
    j = 1
    k = 0

    sequencia = [i, j]

    while True:
        if n > sequencia[-1]:
            k = i + j
            sequencia.append(k)
            i = j
            j = k

        elif n < sequencia[-1]:
            return print("Esse numero nao faz parte da sequencia de fibonacci")
        else:
            return print(sequencia)

# n = int(input("Numero: "))
# fibonacci(n)
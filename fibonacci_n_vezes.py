def fibonacci(n):
    i = 0
    j = 1
    k = 0

    sequencia = [i, j]
        
    while len(sequencia) < n:
        k = i + j
        sequencia.append(k)
        i = j
        j = k

    return {
        "Sequência": str(sequencia)
    }

# n = int(input("Numero: "))
# fibonacci(n)
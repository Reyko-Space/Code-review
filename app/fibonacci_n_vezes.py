def fibonacci(n):
    i = 0
    j = 1
    k = 0

    sequence = [i, j]
        
    while len(sequence) < n:
        k = i + j
        sequence.append(k)
        i = j
        j = k

    return {
        "Sequência": str(sequence)
    }

# n = int(input("Numero: "))
# fibonacci(n)
def fibonacci(n):
    i = 0
    j = 1
    k = 0

    sequence = [i, j]

    while True:
        if n > sequence[-1]:
            k = i + j
            sequence.append(k)
            i = j
            j = k

        elif n < sequence[-1]:
            return {
                "Erro": "Esse numero não faz parte da sequência de fibonacci!"
            }
        else:
            return {
                "Sequência": str(sequence)
            }

# n = int(input("Numero: "))
# fibonacci(n)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return ("Estou saudável!")

@app.post("/fibonacci/ate_n/{n}")
def fibonacci_ate_n(n: int):
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
        
@app.post("/fibonacci/n_vezes/{n}")
def fibonacci_n_vezes(n: int):
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

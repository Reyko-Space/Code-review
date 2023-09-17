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

    sequencia = [i, j]

    while True:
        if n > sequencia[-1]:
            k = i + j
            sequencia.append(k)
            i = j
            j = k

        elif n < sequencia[-1]:
            return "Esse numero não faz parte da sequência de fibonacci!"
        else:
            return {
                "Sequência": str(sequencia)
            }
        
@app.post("/fibonacci/n_vezes/{n}")
def fibonacci_n_vezes(n: int):
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
        
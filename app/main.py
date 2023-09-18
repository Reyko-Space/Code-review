from fastapi import FastAPI
from fibonacci_ate_n import fibonacci as fibonacci_ate_n
from fibonacci_n_vezes import fibonacci as fibonacci_n_vezes

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return ("Estou saudável!")

@app.post("/fibonacci/ate_n/{n}")
def fib_ate_n(n: int):
    return fibonacci_ate_n(n)
        
@app.post("/fibonacci/n_vezes/{n}")
def fib_n_vezes(n: int):
    return fibonacci_n_vezes(n)

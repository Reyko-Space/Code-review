FROM python:3.11-bullseye

WORKDIR /usr/src/myApp

COPY requirements.txt \
    /app/fibonacci_n_vezes.py \
    /app/fibonacci_ate_n.py \
    /app/main.py \
    /usr/src/myApp/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
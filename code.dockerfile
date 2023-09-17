FROM python:3.11-bullseye

WORKDIR /app

COPY requirements.txt ./\
    app/main.py ./ /app/

COPY . /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
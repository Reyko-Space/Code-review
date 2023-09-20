FROM python:3.11-bullseye

WORKDIR /project

COPY requirements.txt ./app ./project/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
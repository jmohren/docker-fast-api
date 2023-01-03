FROM python:3.7-slim

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./model ./model
COPY main.py .

CMD ["python", "main.py"]
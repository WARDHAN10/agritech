FROM python:3.9-alpine

WORKDIR /app

COPY main.py /app/main.py

CMD ["python", "/app/main.py"]
FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask==2.0.1 werkzeug==2.0.1

EXPOSE 5000

CMD ["python", "app.py"]
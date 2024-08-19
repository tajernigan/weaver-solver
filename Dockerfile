FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY . .

CMD ["python", "-m", "unittest", "discover", "tests"]

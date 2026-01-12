FROM python:3.13-slim

WORKDIR /app

COPY emp.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "emp.py", "101", "basavaraj", "28"]

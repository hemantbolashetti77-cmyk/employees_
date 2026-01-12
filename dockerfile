
FROM python:3.12-slim

WORKDIR /emp

COPY . .

CMD [ "python" , "emp.py"]

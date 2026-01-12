
FROM python:3.12-slim

WORKDIR /employee

COPY . .

CMD [ "python" , "employee.py"]
FROM python:3.9-slim

WORKDIR /tests

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD behave features/ -f html -o reports/${BROWSER}_report.html
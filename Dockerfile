FROM python:3.11.0-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc postgresql-client
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x run_etl.sh
RUN chmod +x wait-for-postgres.sh

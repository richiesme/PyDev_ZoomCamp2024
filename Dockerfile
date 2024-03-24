FROM python:3.11

RUN apt-get install wget
RUN pip install pandas pyarrow sqlalchemy psycopg2

WORKDIR /myApp

COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]


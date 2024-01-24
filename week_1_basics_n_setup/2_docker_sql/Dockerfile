FROM python:3.10

RUN pip install pandas pyarrow

WORKDIR /myApp

COPY pipeline.py pipeline.py

ENTRYPOINT [ "python", "pipeline.py" ]
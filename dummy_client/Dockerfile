FROM python:3.10

WORKDIR /client

COPY ./requirements.txt /client/requirements.txt

RUN pip install -r requirements.txt

COPY ./dummy_client /client/dummy_client

CMD ["python", "dummy_client/client.py"]
FROM python:3.10

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install -r requirements.txt

COPY ./alembic.ini /backend/alembic.ini

COPY ./docker /backend/docker

COPY ./dummy_server /backend/dummy_server

RUN chmod a+x /backend/docker/*.sh

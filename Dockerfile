FROM python:3

ENV PYTHONBUFFERED=1

WORKDIR /ecomm_api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
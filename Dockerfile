FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY . /code/

CMD ["gunicorn", "rezarezaeeshp.wsgi","--bind", "0.0.0.0:8000"]



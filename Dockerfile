FROM python:3.8-slim-buster

RUN apt-get update --yes

RUN pip3 install -U pip

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY utils.py utils.py
COPY main.py main.py
COPY artifacts artifacts
COPY client client

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "gunicorn", "-b", "0.0.0.0:8000", "main:app", "--workers=5"]

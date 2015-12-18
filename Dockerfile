FROM python:2.7

MAINTAINER Charles Sartori <charles.sartori@gmail.com>

COPY . /app

WORKDIR /app/output/

RUN pip install -r /app/requirements.txt

CMD python -m pelican.server

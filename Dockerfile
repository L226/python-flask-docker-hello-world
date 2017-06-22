FROM python:2.7
MAINTAINER lfries@cozero.com.au

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-w", "1", "-b", ":8080", "--log-level", "info", "-t", "60", "app:app", "--worker-class", "gevent"]
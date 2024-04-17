FROM python:3.10

WORKDIR /app

COPY ./app .

EXPOSE 5000
 
RUN pip install flask

RUN pip install faker

RUN pip install tabulate

CMD flask --app server run --host=0.0.0.0

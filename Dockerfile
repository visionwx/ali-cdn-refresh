FROM python:3.9.1

WORKDIR /app

COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ./src .

CMD [ "python", "/app/main.py" ]
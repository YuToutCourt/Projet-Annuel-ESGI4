FROM alpine:latest

RUN apk update && apk upgrade

RUN apk add --no-cache python3 py3-pip && \ 
    pip install django --break-system-packages

RUN mkdir /code
WORKDIR /code

COPY ./app/ /code/

WORKDIR /code/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
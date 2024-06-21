FROM alpine:latest

RUN apk update && apk upgrade

RUN apk add --no-cache python3 py3-pip && \
    pip install aiosmtpd --break-system-packages

RUN mkdir /site
WORKDIR /site

COPY ./site/ /site/

WORKDIR /site/

EXPOSE 8080
EXPOSE 25

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]

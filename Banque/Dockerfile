FROM alpine:latest

RUN apk update && apk upgrade

RUN apk add --no-cache python3 py3-pip && \
    pip install aiosmtpd --break-system-packages && \
    pip install flask --break-system-packages && \
    pip install requests icecream  --break-system-packages 

RUN mkdir /site
RUN mkdir /mail
WORKDIR /site

COPY ./site/ /site/
COPY ./mail/ /mail/

WORKDIR /site/

EXPOSE 8080
EXPOSE 25

ENV KEY FarBanK

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]

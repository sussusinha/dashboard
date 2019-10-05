
FROM ubuntu

WORKDIR /app

RUN apt update && apt install apache2 -y

COPY entrypoint.sh /app/entrypoint.sh

COPY html /var/www/html

CMD [ "/bin/sh", "/app/entrypoint.sh" ]

#!/bin/bash

echo "Iniciando o serviço do apache ..."
service apache2 start

echo "Amarrando o container ao access log ..."
tail -f /var/log/apache2/access.log
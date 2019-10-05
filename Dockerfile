
FROM ubuntu

WORKDIR /app

RUN apt update && apt install -y \
    vim \
    python3-pip

COPY requirements.txt /app/requirements.txt 

RUN pip3 install -r /app/requirements.txt

COPY . /app

CMD [ "python3", "/app/app.py" ]


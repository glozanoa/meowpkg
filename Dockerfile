FROM python:alpine

WORKDIR /pyapp
COPY . /pyapp

RUN python3 -m pip install .

ENTRYPOINT ["dragon-cowsay"]

FROM       python:3.7.4

WORKDIR    /var/app

EXPOSE     8080

RUN        apt-get update && apt-get install --yes libev-dev
RUN        pip install bjoern

ADD        ./MTAPI/requirements.txt /var/app/requirements.txt

RUN        pip install -r /var/app/requirements.txt

ADD        ./MTAPI /var/app
ADD        ./server.py /var/app
ADD        ./settings_env.py /var/app

CMD        []
ENTRYPOINT MTAPI_SETTINGS=settings_env.py python server.py

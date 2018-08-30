FROM python:3.6

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY ./src/requirements.txt /opt/app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /opt/app

CMD ["python", "server.py"]

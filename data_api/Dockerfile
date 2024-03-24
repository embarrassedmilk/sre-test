FROM python:3.10

WORKDIR /data_app
COPY requirements.txt /data_app

RUN pip3 install -r requirements.txt

COPY . /data_app

ENTRYPOINT ["python3"]
CMD ["app.py"]
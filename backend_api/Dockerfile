FROM python:3.10

WORKDIR /backend_app
COPY requirements.txt /backend_app

RUN pip3 install -r requirements.txt

COPY . /backend_app

ENTRYPOINT ["python3"]
CMD ["app.py"]
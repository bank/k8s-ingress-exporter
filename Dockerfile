FROM python:3.6.5-stretch
WORKDIR /app

WORKDIR /app/src
COPY requirements.txt /app/src
RUN pip3 install -r requirements.txt

COPY app.py /app/src
CMD ["python3", "-u", "app.py"]

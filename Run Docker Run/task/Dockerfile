FROM python:3.11-slim

LABEL author=HyperUser

EXPOSE 8000

WORKDIR /home/app

ADD /hyper-app/requirements.txt .
ADD /hyper-app/main.py .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
FROM python:3.6

ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

RUN apt-get update && apt-get -y install python-dev musl-dev gcc git libev-dev netcat build-essential && apt-get clean
# RUN pip install --upgrade pip


COPY app ./app
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh ./
RUN chmod +x ./start.sh

CMD watchmedo auto-restart --recursive --pattern="*.html;*.js;*.py" --directory="." /bin/bash start.sh
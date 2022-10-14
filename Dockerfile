FROM ubuntu:latest

RUN apt-get update && apt-get install -y cron python3 python3-pip

WORKDIR /home/embassy

COPY . .

RUN pip3 install -r requirements.txt

COPY crontab /etc/cron.d/crontab

RUN chmod 777 schedule.sh
RUN chmod 777 /etc/cron.d/crontab && crontab /etc/cron.d/crontab

RUN cron

CMD service cron restart

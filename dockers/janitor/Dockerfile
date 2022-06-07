FROM ubuntu:latest

RUN apt-get update && apt-get -y install cron && apt-get -y install docker-compose

RUN mkdir /logs

COPY cron/cronTable /etc/cron.d/cronTable
RUN chmod 0644 /etc/cron.d/cronTable
RUN crontab /etc/cron.d/cronTable

COPY ./content /content
COPY ./script /script

CMD cron && /script/start.sh && while true; do sleep 10000; done

#docker run --rm -d -v /c/Users/kissa/GoogleDrive/Sources/Constellation/janitor/logs:/logs -v /var/run/docker.sock:/var/run/docker.sock xannosz/janitor
#docker rm -f `docker ps -a | awk '{print $1}'`
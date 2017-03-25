#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd mainapp  
# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
su -m myuser -c "python celery worker -A celeryapp -Q default -n default@%h"
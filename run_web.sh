#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
PIDPATH="/tmp/uwsgi.pid"
#if [ -f ${PIDPATH} ]
#then
#    uwsgi --stop ${PIDPATH}
#fi
gunicorn -c gunicorn.ini LianHua.wsgi
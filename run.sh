#!/bin/bash
set -e
NUM_WORKERS=3
USER=root
GROUP=root
cd /home/www/scircle_judge
. /home/www/scircle_judge/env/bin/activate
cd scircle_judge
test -d /var/log/scircle_judge || mkdir -p /var/log/scircle_judge
exec gunicorn -w  $NUM_WORKERS -b 0.0.0.0:8005 \
config.wsgi:application
--user=$USER --group=$GROUP 
	--log-level=debug \
    --log-file=/var/log/scircle_judge/scircle_judge.log 2 >>/var/log/scircle_judge/scircle_judge.log


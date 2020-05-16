#!/usr/bin/env python

import os

from bottle import route, run, template
import redis
import socket


@route('/')
def index():
    # Conexion a Redis
    #rd = redis.Redis(host='localhost', port=6379, db=0) # Localhost
    #rd = redis.Redis(host='redis', port=6379, db=0) # Hardcode
    redis_server = os.environ['redis'].replace('"', '')
    rd = redis.Redis(host=redis_server, port=6379, db=0) # Environment variable

    # Counter
    rd.incr("mycounter")
    my_counter = rd.get("mycounter")
    rd.close()

    # Hostname
    my_host = socket.gethostname()
    # App version
    f = open("/etc/app_version", "r")
    app_version = f.read()

    return template('MY_KEY {{my_value}}</br> Counter: {{counter}}</br></br>Host: {{host}}</br>Version: {{version}}', \
        my_value=os.environ['MY_KEY'], counter=my_counter, host=my_host, version=app_version)

run(host='0.0.0.0', port=8080, debug=True) #dev
#run(host='0.0.0.0', port=8080) #prod

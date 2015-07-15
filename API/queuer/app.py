#!/usr/bin/env python

import datetime
import threading
import time
import json
import random
import re
from Queue import Queue
from bottle import route, hook, response, run, static_file, request

url_cache = {}

@route('/')
def index():
    return 'Not found'

@route('/push', method = 'GET')
def push():
    url = request.params.get('url','')
    # does url need to be urldecoded
    if 'http' not in url:
        return 'Error'
    if url in url_cache:
        return url_cache[url]
    url_cache[url] = len(data_structure)
    data_structure.append({'input':url, 'output':''})
    todo.put(url)
    return url_cache[url]

@route('/status/<place>')
def status(place='0'):
    try:
        numplace = int(place)
    except:
        return 'Error'
    if len(data_structure) > numplace:
        return data_structure[numplace]['output']
    return 'Error'

@route('/update/<place>/<output>')
def update(place='x', output='x'):
    # how does remote ip look for localhost
    remote_ip = request.environ.get('REMOTE_ADDR')
    print remote_ip
    try:
        numplace = int(place)
        if remote_ip not in workers:
            raise
    except:
        return 'Error'
    data_structure[numplace]['output'] = output
    workers_available[remote_ip] = True

run(host = '0.0.0.0', port = 8080, server = 'tornado')

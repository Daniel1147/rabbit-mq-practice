#!/usr/bin/env python
import pika
import sys
from datetime import datetime

def add_time(message):
    time_str = datetime.now().strftime("%H:%M:%S")
    return  '({}) {}'.format(time_str, message)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# message
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = add_time(message)

# publish to the exchange
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()

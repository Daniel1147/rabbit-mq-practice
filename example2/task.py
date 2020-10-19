#!/usr/bin/env python
import pika
from datetime import datetime
import sys


# channel
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()
channel.queue_declare(queue='hello')

# message
message = ' '.join(sys.argv[1:]) or 'Hellow world..'
message = '({}) {}'.format(datetime.now().strftime("%H:%M:%S"), message)

# fire
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent '{}'".format(message))

connection.close()

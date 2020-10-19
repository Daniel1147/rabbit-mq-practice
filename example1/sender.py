#!/usr/bin/env python
import pika
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = '({}) Hello World!'.format(datetime.now().strftime("%H:%M:%S"))
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent '{}'".format(message))
connection.close()

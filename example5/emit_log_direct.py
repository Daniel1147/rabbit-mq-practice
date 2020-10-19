#!/usr/bin/env python
import pika
import sys

message_list = [
    ['cron', 'critical', 'm1'],
    ['cron', 'info', 'm2'],
    ['kern', 'info', 'm3'],
    ['kern', 'critical', 'm4'],
    ['auth', 'critical', 'm5'],
    ['auth', 'warn', 'm6'],
]

# get connection, channel
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# send messages
for message in message_list:
    [f, s, m] = message
    channel.basic_publish(exchange='topic_logs', routing_key='{}.{}'.format(f, s), body=m)
    print(" [x] send {}-{}: {}".format(f, s, m))

connection.close()

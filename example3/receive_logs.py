#!/usr/bin/env python
import pika, sys, os

def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode())

def main():
    exchange = 'logs'
    exchange_type = 'fanout'

    # channel
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # make sure the exchange exists
    channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)

    # get a queue with random name
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # bind queue and exchange
    channel.queue_bind(exchange=exchange, queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

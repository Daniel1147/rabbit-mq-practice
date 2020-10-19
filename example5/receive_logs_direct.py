#!/usr/bin/env python
import pika, sys, os

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body.decode()))


def main():
    # get connection, channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    # new queue
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    for binding_key in sys.argv[1:]:
        channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
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

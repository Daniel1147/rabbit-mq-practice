#!/usr/bin/env python
#!/usr/bin/env python
import pika, sys, os
import time

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done ")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    # channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    # set consume
    channel.basic_consume(queue='hello', on_message_callback=callback)

    # start consuming
    print(' [*] Waiting for messages. To exit press CTRL+C')
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

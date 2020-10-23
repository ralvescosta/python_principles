import os
import sys
import pika


def connect_to_amqp() -> any:
    amqp_connection_params = (
        pika.URLParameters("amqp://rabbitmq:123456@127.0.0.1:5672")
    )
    connection = pika.BlockingConnection(amqp_connection_params)
    return connection.channel()


def register_amqp_channel(amqp_client, cb) -> None:
    amqp_client.basic_consume(queue="queue",
                              auto_ack=True,
                              on_message_callback=cb)


def received_amqp_message(ch, method, properties, body):
    print(" [x] Received %r" % body)


if __name__ == '__main__':

    try:
        print("Start AMQP Connection...")
        channel = connect_to_amqp()
        print("Connected...")

        print("Register channels listener...")
        register_amqp_channel(channel, received_amqp_message)
        print("Already....")
        channel.start_consuming()
        print("[*] Waiting for messages. To exit press CTRL+C")

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

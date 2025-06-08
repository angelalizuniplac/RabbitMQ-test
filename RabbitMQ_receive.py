import pika, sys, os

def main():

    credentials = pika.PlainCredentials('user', 'password') # 'guest', 'guest'
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='filaTeste')

    def callback(ch, method, properties, body):
        print("Recebida: %r" % body)

    channel.basic_consume(queue='filaTeste', on_message_callback=callback, auto_ack=True)

    print('Aguardando mensagens. To exit press CTRL+C')
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

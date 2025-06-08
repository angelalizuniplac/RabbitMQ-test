#!/usr/bin/env python
import pika
import random


credentials = pika.PlainCredentials('user', 'password')  # 'guest', 'guest'
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='filaTeste')  # declara a fila

strEnviar = 'Mensagem ' + str(random.randrange(0, 100, 1))

# roteia para a fila
channel.basic_publish(exchange='', routing_key='filaTeste', body=strEnviar)


print("Enviada: " + strEnviar)

connection.close()
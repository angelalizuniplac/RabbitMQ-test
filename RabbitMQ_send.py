# Shebang: indica que este script deve ser executado com o interpretador Python
# Permite executar o arquivo diretamente no terminal: ./script.py
#!/usr/bin/env python

import pika # Importa a biblioteca Pika para comunicação com RabbitMQ
import random # Importa biblioteca para gerar números aleatórios

# CONFIGURAÇÃO DA CONEXÃO
# Cria credenciais de autenticação para conectar ao RabbitMQ
credentials = pika.PlainCredentials('user', 'password')  # 'guest', 'guest' 

# Define os parâmetros de conexão:
# - 'localhost': endereço do servidor RabbitMQ (servidor local)
# - 5672: porta padrão do RabbitMQ para conexões AMQP
# - '/': virtual host padrão (como um namespace) Ex.: /app-vendas, /app-estoque, /prod, dev etc...
# - credentials: as credenciais criadas acima
parameters = pika.ConnectionParameters('localhost', 5672, 'dev', credentials)

# Estabelece conexão SÍNCRONA com o RabbitMQ usando os parâmetros
# BlockingConnection fica "travado" aqui até conseguir conectar
# Só continua quando a conexão for estabelecida ou der erro
connection = pika.BlockingConnection(parameters)
# FIM DA CONFIGURAÇÃO DA CONEXÃO

# CONFIGURAÇÃO DO CANAL

# Cria um canal de comunicação dentro da conexão
# Canal é onde realmente acontecem as operações (enviar/receber mensagens)
channel = connection.channel()

# Declara/cria uma fila chamada 'filaTeste'
# Se a fila já existir, nada acontece
# Se não existir, ela é criada
channel.queue_declare(queue='filaTesteDev')  # declara a fila
#FIM DA CONFIGURAÇÃO DO CANAL

# PREPARAÇÃO DA MENSAGEM
#Monta o conteudo que será dentro do pacote de mensagem
strEnviar = 'Mensagem ' + str(random.randrange(0, 100, 1))
# FIM DA PREPARAÇÃO DA MENSAGEM

# ENVIO DA MENSAGEM
# Publica/envia a mensagem para a fila:
#exchange recebe mensagens de produtores e decide para quais filas elas devem ser entregues
# - exchange='': usa o exchange padrão (direct exchange)
# - routing_key='filaTeste': nome da fila de destino
# - body=strEnviar: conteúdo da mensagem a ser enviada
channel.basic_publish(exchange='', routing_key='filaTeste', body=strEnviar)
# Se você quiser enviar a mesma mensagem para várias filas ao mesmo tempo, o exchange padrão não serve e
# precisar criar um exchange customizado, ex: channel.exchange_declare(exchange='log', exchange_type='fanout')
# fanout = broadcast

print("Enviada: " + strEnviar)

# Fecha a conexão com RabbitMQ
connection.close()
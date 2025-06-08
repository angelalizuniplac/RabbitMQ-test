# pika: biblioteca para comunicação com RabbitMQ
# sys: funções do sistema (usado para sair do programa)
# os: funções do sistema operacional (usado para forçar saída)
import pika, sys, os

def main():
    # Cria credenciais de autenticação para conectar ao RabbitMQ
    credentials = pika.PlainCredentials('user', 'password') # 'guest', 'guest'

    # Define os parâmetros de conexão com RabbitMQ
    # - 'localhost': endereço do servidor RabbitMQ (servidor local)
    # - 5672: porta padrão do RabbitMQ para conexões AMQP
    # - '/': virtual host padrão (como um namespace)
    # - credentials: as credenciais criadas acima
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

    # Estabelece conexão SÍNCRONA com o RabbitMQ usando os parâmetros
    # BlockingConnection fica "travado" aqui até conseguir conectar
    # Só continua quando a conexão for estabelecida ou der erro
    connection = pika.BlockingConnection(parameters)

    # Cria um canal de comunicação dentro da conexão
    channel = connection.channel()

    # Declara/cria uma fila chamada 'filaTeste'
    # Se a fila já existir, nada acontece. Se não existir, ela é criada
    channel.queue_declare(queue='filaTeste')

    # Cria função para processar mensagens recebidas
    # 1. ch (Channel) - O canal que recebeu a mensagem
    #    Útil para: enviar confirmações, publicar respostas, etc.

    # 2. method (Method) - Informações sobre como a mensagem foi entregue
    #    Contém: delivery_tag, routing_key, exchange, etc.

    # 3. properties (Properties) - Metadados da mensagem
    #    Contém: content_type, headers, timestamp, message_id, etc.

    # 4. body - O conteúdo real da mensagem (bytes)é o que conteudo para processar
    def callback(ch, method, properties, body):
        print("Recebida: %r" % body)
    # obs: % É o operador de formatação de strings em Python.
    #ex: %r mostra como string, %s mostra sem aspas(amigavel), %d formata com numeros inteiros

    # Configura o consumidor para escutar a fila
    # queue: nome da fila a ser monitorada
    # on_message_callback: função a ser chamada quando receber mensagem
    # auto_ack=True: confirma automaticamente o recebimento da mensagem
    channel.basic_consume(queue='filaTeste', on_message_callback=callback, auto_ack=True)

    print('Aguardando mensagens. To exit press CTRL+C')

    # Inicia o loop de consumo de mensagens
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:       
        print('Interrupted') # Captura interrupção por teclado (Ctrl+C)
        try:           
            sys.exit(0) 
        except SystemExit:           
            os._exit(0)  # Se a saída normal falhar, força a saída

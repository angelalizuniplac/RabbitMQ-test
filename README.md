# Requisitos: 

Baixar imagem do Rabbitmq para rodar em docker: 

```docker run -d --restart=always --hostname rabbitmq --name rabbitmq -p 8080:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:4.1-management-alpine```

# Ambiente virtual 
1. Criar um ambiente virtual para isolar o projeto:

    ```python -m venv venv```

2. Ativar o ambiente:

    ```venv\Scripts\activate```

3. Instalar a biblioteca Pika no ambiente virtual

    ```pip install pika --upgrade```

# Execução 
Agora é só executar: 

Execute o script de envio para fila e observe as mensagens chegando na fila.  
    ```python RabbitMQ_send.py```

Execute o script de recebimento da fila e observe as mensagens sendo consumidas, ou seja, saindo da fila: 

```python RabbitMQ_receive.py```
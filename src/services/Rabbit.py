from amqpstorm import Connection
from amqpstorm import Message
import logging


logging.basicConfig(level=logging.DEBUG)


def postMessage(host, user, passwor, vh, queue, file):
    connection = Connection(host, user, passwor,virtual_host = vh)

    channel = connection.channel()

    data = open(file, 'r')

    properties = {'content_type': 'application/json'}

    logging.info('Realizando o envio de payloads %s para a fila %s', file, queue)    
    contador = 0
    for body in data:    
        message = Message.create(channel=channel, body=body, properties=properties)
        message.publish(routing_key=queue)
        contador+=1

    logging.warning('Envio finalizado de %i',contador)

    return 'Envio finalizado com sucesso: '+ str(contador)
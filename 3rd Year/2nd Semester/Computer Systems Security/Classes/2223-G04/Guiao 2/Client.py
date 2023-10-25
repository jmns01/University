# Código baseado em https://docs.python.org/3.6/library/asyncio-stream.html#tcp-echo-client-using-streams
import asyncio
import socket
import json
from Crypto.Cipher import ChaCha20
from base64 import b64encode
from Crypto.Random import get_random_bytes


conn_port = 7777
max_msg_size = 9999

class Client:
    """ Classe que implementa a funcionalidade de um CLIENTE. """
    def __init__(self, sckt=None):
        """ Construtor da classe. """
        self.sckt = sckt
        self.msg_cnt = 0

    def encrypt(self, txt = b''):
        key = b'p9-\x96\xe6>V\x06\xd3\x93I\x14!\xeb\x8cD\xdd\xc9\xb6dM\x0e\x1fn\xa3\xae%n\xd9\xd2\xd0Y'
        cipher = ChaCha20.new(key=key)

        ciphertext = cipher.encrypt(txt)
        ct = b64encode(ciphertext).decode('utf-8')
        nonce = b64encode(cipher.nonce).decode('utf-8')
        result = json.dumps({'nonce':nonce, 'ciphertext':ct})

        return result.encode()


    def process(self, msg=b""):
        """ Processa uma mensagem (`bytestring`) enviada pelo SERVIDOR.
            Retorna a mensagem a transmitir como resposta (`None` para
            finalizar ligação) """
        self.msg_cnt +=1
        #
        # ALTERAR AQUI COMPORTAMENTO DO CLIENTE
        #
        print('Received (%d): %r' % (self.msg_cnt , msg.decode()))
        print('Input message to send (empty to finish)')
        new_msg = input().encode()
        new_msg = self.encrypt(new_msg)
        print(new_msg)
        #
        return new_msg if len(new_msg)>0 else None



#
#
# Funcionalidade Cliente/Servidor
#
# obs: não deverá ser necessário alterar o que se segue
#


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', conn_port)
    addr = writer.get_extra_info('peername')
    client = Client(addr)
    msg = client.process()
    while msg:
        writer.write(msg)
        msg = await reader.read(max_msg_size)
        if msg :
            msg = client.process(msg)
        else:
            break
    writer.write(b'\n')
    print('Socket closed!')
    writer.close()

def run_client():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client())


run_client()

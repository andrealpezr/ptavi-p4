#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys


if len(sys.argv) < 6:
    sys.exit('Usage: python3 client.py ip puerto '
             'register sip_address expires_value')

# Constantes. Dirección IP del servidor:
SERVER = sys.argv[1]
PORT = int(sys.argv[2])

# Contenido que vamos a enviar
USER = sys.argv[4]
EXPIRES = int(sys.argv[5])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", USER)
    if sys.argv[3] == 'register':
        my_socket.send(bytes('REGISTER sip:' + USER + ' SIP/2.0\r\nExpires: ' +
                             EXPIRES + '\r\n\r\n', 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")

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
EXPIRES = sys.argv[5]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    if sys.argv[3] == 'register':
        mensaje = ('REGISTER sip:' + USER + ' SIP/2.0\r\n')
        mensaje += ('EXPIRES: ' + EXPIRES + '\r\n\r\n')
        print(mensaje)
        my_socket.send(bytes(mensaje, 'utf-8'))
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
    print("Socket terminado.")

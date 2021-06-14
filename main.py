#!/usr/bin/env python3

import socket

HOST = 'gopher.floodgap.com'
PORT = 70

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'\r\n')
    data = ""
    while '\r\n.\r\n' not in data:
        data += s.recv(1024).decode('ascii')
table = []
rows = data.splitlines()
for i in rows:
    segments = i.split('\t')
    table.append(segments)

for r in table:
    if len(r) > 1:
        usertext = r[0]
        print(usertext[1:len(usertext)])

#print(repr(data))

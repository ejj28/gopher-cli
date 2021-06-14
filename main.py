#!/usr/bin/env python3

import socket

DEFAULT_PORT = 70

def userInput():
    inputstring = input("COMMAND: ")
    args = inputstring.split()
    if len(args) == 0:
        raise ValueError('ERROR: No Command was entered.')
    elif args[0] == "connect":
        if len(args) == 2:
            try:
                data = retrieve(args[1], DEFAULT_PORT)
            except Exception as error:
                raise Exception("ERROR: Connection failed")
            display(data)
        elif len(args) == 3:
            try:
                data = retrieve(args[1], int(args[2]))
            except Exception as error:
                raise Exception("ERROR: Connection failed")
            display(data)
        else:
           raise ValueError('ERROR: Incorrect number of parameters entered.') 
    elif args[0] == "exit":
        print("Exiting..")
        exit()
    else:
        raise ValueError('ERROR: The entered command is not valid.')


def retrieve(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(b'\r\n')
            data = ""
            while '\r\n.\r\n' not in data:
                data += s.recv(1024).decode('ascii')
    except:
        raise Exception()
    table = []
    rows = data.splitlines()
    for i in rows:
        segments = i.split('\t')
        table.append(segments)
    return table

def display(inTable):
    for r in inTable:
        if len(r) > 1:
            usertext = r[0]
            print(usertext[1:len(usertext)])
try:
    while True:
        try:
            userInput()
        except ValueError as error:
            print(error)
        except Exception as error:
            print(error)
except KeyboardInterrupt:
    print("\nExiting..")

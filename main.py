#!/usr/bin/env python3

import socket
from termcolor import colored

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
    print("\n")
    for r in inTable:
        text = r[0]
        if text[0] == "0" or text[0] == "1":
            print(colored(text[1:len(text)], "cyan"))
        else:
            print(text[1:len(text)])
try:
    while True:
        try:
            userInput()
        except ValueError as error:
            print(colored(error, "red"))
        except Exception as error:
            print(colored(error, "red"))
except KeyboardInterrupt:
    print("\nExiting..")

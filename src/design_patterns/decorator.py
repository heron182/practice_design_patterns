import gzip
import logging
import socket
import time
from io import BytesIO

logging.basicConfig(level=logging.INFO)

LOG_INFO = False
GZIP_MODE = True


# third party library code decorated
def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()


def socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 2401))
    server.listen(1)
    try:
        while True:
            client, addr = server.accept()
            if LOG_INFO:
                respond(LogSocket(client))
            elif GZIP_MODE:
                respond(GzipSocket(client))
            else:
                respond(client)
    finally:
        server.close()


def socket_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 2401))
    print("Received: {0}".format(client.recv(1024)))
    client.close()


class LogSocket(object):
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        logging.info('Sending message %s', data)
        self.socket.send(data)

    def close(self):
        self.socket.close()


class GzipSocket(object):
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode='w')
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()


# decorated user created functions
def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__, args,
                                                    kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(func.__name__, time.time() - now))
        return return_value

    return wrapper


def test1(a, b, c):
    print("\ttest1 called")


def test2(a, b):
    print("\ttest2 called")


@log_calls
def test3(a, b):
    print("\ttest3 called")
    time.sleep(1)


test1 = log_calls(test1)
test2 = log_calls(test2)
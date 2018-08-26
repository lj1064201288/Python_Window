import socket
from urllib import request, error

if __name__ == '__main__':
    try:
        response = request.urlopen('http://httpbin.org/get',timeout=0.1)
    except error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')
        
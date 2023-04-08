##sql注入常见关键字:

select, show, union, concat, columns, tables, desc, limit, databases, ascii,
substr, length, @@VERSION, PREPARE, EXECUTE, sleep, group_concat, order by, user,
updatexml, extractvalue, floor

##过滤绕过:
空格: /**/, (), %20, %09, %0a, %0b, /*!*/

###常规注入:
大部分sql注入题使前方语句闭合后可使用show databases进行数据库查询,使用show @@VERSION可查询到系统版本信息等,
使用show tables可获得当前数据库下所有表,使用desc表名可获得表的列名,使用union可进行多语句查询,使用show user()
即可获得用户名

###盲注:
注意事项：尽量使用二分法提升效率,第一：防止时间不够,第二：防止靶机关闭
有些网站存在注入漏洞,回显只有两种状态,攻击者可使用ascii, substr, length等关键字通过ascii码的方式进行盲注
有些网站存在注入漏洞,没有回显,攻击者可通过sleep使用时间作为回显进行盲注

###报错注入:
注意: 报错注入对于mysql的版本有要求
报错注入产生原因: 正常注入 --> 回显正常 在报错的内容中存在数据库中数据
                  报错注入 --> 回显报错

常见使用方式: 闭合语句后使用updatexml(1, concat(0x7e, **databases()**, 0x7e), 1), 由于0x7e不属于xpath语法所以会报错
extractvalue(1,concat(0x7e,**user()**,0x7e,**database()**))
总结: 报错注入有固定格式，将加粗部分更换即可

###预编译:
经常: 会遇到关键字被ban,比如select, 通过预编译的方式即可注入成功，例：buuctf/web/[强网杯]随便住/README.md

###sql注入获取系统权限:
原理: 使用udf提权获取WebShell。也是通过into oufile向服务器写入两个文件，一个可以直接执行系统命令，一个进行上传文件
注意:

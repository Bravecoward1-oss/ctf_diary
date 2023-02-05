web01
首页
![img.png](img/img.png)
发现点击Hint后进入flag.php页面，检查网页源码后发现![img_1.png](img/img_1.png)
![img_2.png](img/img_2.png)
解密后发现h1dden_aurora_hochladen.php目录
![img_3.png](img/img_3.png)
发现文件上传接口, 尝试直接上传php
![img_4.png](img/img_4.png)
上传后发现可能对文件后缀做检测，更改webshell后缀尝试绕过
![img_5.png](img/img_5.png)
上传成功，猜测上传目录就是当前目录，使用bp更改文件后缀

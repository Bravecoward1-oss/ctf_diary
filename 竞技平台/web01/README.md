web02

主要考点：webshell, 条件竞争

首先访问flag.php,打开开发者模式

![img.png](img/img.png)
![img_1.png](img/img_1.png)
![img_2.png](img/img_2.png)

可以发现上传点


上传.png文件后获得文件上传地址/upload


上传.php也是可以的尝试上传后
![img_3.png](img/img_3.png)
更改后缀后
![img_4.png](img/img_4.png)
这时候发现是条件竞争，使用bp重复发送上传和访问包

payload:
![img_5.png](img/img_5.png)
![img_6.png](img/img_6.png)
![img_7.png](img/img_7.png)

![img_8.png](img/img_8.png)
![img_9.png](img/img_9.png)
![img_10.png](img/img_10.png)
![img_11.png](img/img_11.png)

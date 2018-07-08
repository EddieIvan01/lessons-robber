## CUMT多线程公选课抢课脚本

**Demo**
![](https://upload-images.jianshu.io/upload_images/11356161-9d4ba3a89d6d8637.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***

**How To Use**

+ 下载本仓库文件与[CUMT教务系统模拟登录](https://github.com/EddieIvan01/Analog_Login)文件置于与同一文件夹下

+ 修改config.json，填入教务系统用户名，密码，与欲选课程代号，
e.g.

![](https://upload-images.jianshu.io/upload_images/11356161-7009588876ac3fad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

+ 启动程序，输入启动的线程数。设定只能小于8（为学校的土豆服务器考虑）

***

对于无余量的课程，可以挂在电脑上，持续监控，大概是这样的画面
![](https://upload-images.jianshu.io/upload_images/11356161-96e12173538f401a.gif?imageMogr2/auto-orient/strip)

长时间监控可能会有Cookie过期问题，写了针对代码，但未试验，暂时不能保证长时间监控不会出Bug

***

P.s. 部分post变量代号还不清楚，程序可能不具有不同学院不同年级的普适性。如有疑问，请联系whoami9894@gmail.com


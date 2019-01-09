## CUMT多线程公选课抢课脚本

### NOTICE!!!

2019/1/9 已验证具有不同年级不同专业的普适性，可放心使用

抢课有几率出现`课程代号错误，请查验课程代号`，如果您确保课程代号无误，那么是教务系统`Cookie`的*Bug*，请使用浏览器手动登录一次教务系统，再运行程序抢课

#### Demo

![](https://upload-images.jianshu.io/upload_images/11356161-9d4ba3a89d6d8637.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

***

#### How To Use

+ 安装依赖包：`pip install -r requirements.txt`

+ 修改config.json，填入教务系统用户名，密码，与欲选课程代号，
  e.g.

![](https://upload-images.jianshu.io/upload_images/11356161-7009588876ac3fad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

+ 启动程序

***

#### Status Code

+ INFO中的请求成功指请求服务器成功并接收响应成功，正常状态下会一直看到`请求成功`和`异常`
+ 解释状态码：

  + `1,6D410DC519E6029AE053C0A86D5CEAA6,100,0`为课程无余量

  + 其余状态码都是中文如`课程时间冲突`

***

#### 持续监控

对于无余量的课程，可以挂在电脑上，持续监控，大概是这样的画面

![](https://upload-images.jianshu.io/upload_images/11356161-96e12173538f401a.gif?imageMogr2/auto-orient/strip)

如果有服务器可以使用nohup指令挂载到服务器上，`nohup ./rob.py&`

***

P.s. 部分post变量代号还不清楚，程序可能不具有不同学院不同年级的普适性。如有疑问，请联系whoami9894@gmail.com

***

2018/7/8 16.26   长时间监控时Cookie过期问题已修复

2018/7/8 20.34   发现校园网及移动宽带会出现获取课程信息失败，服务器会返回400 Bad Request（大概是玄学），CSDN上有[同样的问题](https://bbs.csdn.net/topics/390131855)，可能是ISP线路问题导致丢包

2018/7/8 23.58   已打包成exe文件，使用时将`config.json`与rob.exe放于同一文件夹下，启动exe文件即可

2019/1/8 12.51   Hello, 又一个学期的抢课时间，新增异步I/O协程版抢课脚本（Beta版，未验证）

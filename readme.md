### 目录结构
```shell
picture/ #存放爬取的设备图片。
peripheral/ #项目代码。
    api/ #存储项目的API信息。
        __init__.py
        collection.py #收藏接口代码。
        keyboard.py #键盘接口代码。
        lcd.py #显示器接口代码。
        mice.py #鼠标接口代码。
        picture.py #图片接口代码。
        user.py #用户接口代码。
    database/ #存储项目中数据库相关的代码。
        __init__.py
        database.py #存储数据库连接和数据库操作的代码。
        datamodel.py #存储数据库表的模型。
        security.py #存储安全性函数。
    code/ #安装虚拟环境的文件夹。
    utils/ #存储项目的工具函数。
        data/ #存储项目的初始json数据。
        classdemo.py #存储用于数据存储或返回或请求的类。
        导入数据.py #将爬取的数据导入数据库。
        爬取键盘数据.py #从网页爬取键盘数据。
        爬取鼠标数据.py #从网页爬取鼠标数据。
        爬取显示器数据.py #从网页爬取显示器数据。
    main.py #项目的入口文件，负责初始化FastAPI实例和加载路由。
    nohup.out #打印输出的out文件
    setup.py #项目后端启动文件
    requirements.txt #存储项目的依赖项列表。                          
```
### 依赖

1. python 3.9
2. openssl
3. mysql 8.0
等，具体见requirements.txt


### 运行之前


 配置根目录下的sql_config.ini中数据库账户密码

 注意 security不用更改，与token的设置和密码加密有关，其中access_token_expire_minutes表示token有效时间

### 运行
进入虚拟环境
```shell
[root@VM-8-11-centos peripheral]# source code/bin/activate
(code) [root@VM-8-11-centos peripheral]# 

```


1. reload为可选参数,添加表示热加载,即代码更改后会即时反映到服务器上,不用重新输入命令重启服务器

2. 如无法在code目录下运行命令启动接口，则尝试在main.py的上一级目录下运行命令以启动接口

```shell
uvicorn main:app --reload
```

如：(main.py存放在code文件夹中)
```
(code) PS C:\Users\Ronald\Desktop\毕业论文\code> uvicorn main:app --reload
```

**请注意：在运行时保证8000端口没有被占用，当然也可以在上面的命令下加入参数"--port"从而指定端口**

### 接口文档
运行后可通过浏览器访问 http://127.0.0.1:8000/docs 进入接口文档对接口进行测试。 



找出占用端口的进程：

```shell
netstat -anp |grep 端口号
如：netstat -anp |grep 8000

```
杀死进程：
```shell
kill -9 PID
如：kill -9 192465
```
创建虚拟环境(当前目录)：
```shell
python -m venv 虚拟环境名
如：python -m venv code
```
激活虚拟环境：
```shell
source 虚拟环境名/bin/activate
如：source code/bin/activate
```
退出虚拟环境：
```shell
deactivate
```
安装requirements.txt中的依赖：
```shell
pip install -r requirements.txt
```
终端关闭后仍然运行：
```shell
nohup python filename.py &
如：nohup python setup.py &
```
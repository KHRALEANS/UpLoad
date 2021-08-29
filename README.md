# 后端首次运行：
需要建立数据库和手动初始化tables
## 建库：
```
mysql> create database up_load;
```
## 注释掉backend/__init__.py中的以下行：
```angular2html
inject.configure(config_ioc)
```
## 工作目录cd至upload并输入：
```angular2html
$ python
>>> import db
>>> db.init_db()
```
## 后端运行：
```angular2html
$ python app.py
```
## 出现以下提示则表明运行成功：
```angular2html
* Serving Flask app 'backend' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5051/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN:
```

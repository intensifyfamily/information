# information
信息提交

tips
  1.确保电脑中有python-django运行环境和pymysql、cors等库(django2对应pymysql库修改，不清楚看博客：https://blog.csdn.net/qq_43517336/article/details/95737508?utm_source=app)。
  2.进入“DayDayup/DayDayup/"目录下 进入setting.py  修改自己电脑的数据库配置。
  3.运行服务器
      cmd打开"DayDayup/"目录
        #进行数据库迁移
          python manage.py makemigrations
          python manage.oy migrate
        #迁移成功，启动服务器
          python manage.py runserver
    
  4.用浏览器打开”dist/index.html"即可使用
  5.进入admin页面
    cmd打开"DayDayup/"目录
      #创建超级用户
        python manage.py createsuperuser
      #填写相应信息，创建成功重新启动服务器
        python manage.py runserver
    打开浏览器输入本地地址，命令行所示。例（http://127.0.0.1:8000）
    后加上“/admin”，如“http://127.0.0.1:8000/admin”，登录superuser账号密码进入管理
        


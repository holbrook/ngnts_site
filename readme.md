# 下一代交易结算系统服务管理平台

使用Django Rest Framework和AngularJS搭建。参考了 [这篇文章](http://kevinastone.github.io/getting-started-with-django-rest-framework-and-angularjs.html) 以及 [这个项目](https://github.com/kevinastone/django-api-rest-and-angular)。


## 构建

强烈建议使用 `virtualenv` 。

1. 安装需要的python模块

        pip install -r requirements.txt
        python setup.py develop

2. 安装 Bower 和 Grunt

        npm install -g grunt-cli bower

3. 安装依赖的js库

        npm install
        bower install

4. 构建前端页面

        grunt

5. 安装数据库

        make create_database; make make_fixtures

6. 启动服务

        ./manage.py runserver


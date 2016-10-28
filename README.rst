===============================
webapp-flask
===============================

flask web app template.2016-09-24

一个flask
app项目框架，集成了gulp等工具。使用docker集成了redis，mongodb，mysql等数据库，可以快速建立一个flask
app。功能包括coffee，sass支持；前端文件更改后浏览器自动刷新；后端python文件修改后自动重启；docker集成
mysql，mongodb，redis数据库，免去了自己安装的麻烦，可以专注于开发业务逻辑。mac下测试通过。主要参考了以下两个项目生成器：


`generator-webapp <https://github.com/yeoman/generator-webapp>`_
一个前端gulp项目生成器。

`cookiecutter-flask <https://github.com/sloria/cookiecutter-flask>`_
cookiecutter的flask项目生成器。

使用步骤
________

之前需要安装docker, docker-meachine, docker-compose; 用nvm安装node等工具。

.. code-block:: bash

    # mac上先执行一下命令，最后得到的ip是你的访问路径。ubuntu下跳过
    docker-machine start default
    eval $(docker-machine env default)
    docker-machine ip default

之后克隆项目，然后通过npm和bower安装前端相关依赖

.. code-block:: bash

    git clone https://github.com/PegasusWang/flask-app
    cd flask-app/webapp
    npm install    # 安装gulp
    cd webapp/static/
    bower install    # 安装jquery等

最后运行

.. code-block:: bash

   cd flask-app
   docker-compose up    # 启动docker里的flask和数据库等实例
   cd webapp
   gulp serve   # 监控前端等文件

可以直接编写flask应用了。通过 `docker-meachine ip default`
得到的地址访问，然后在gulpfile中代理这个地址。
用 `docker exec -it flaskapp_web_1 bash`
登录进去docker，ctrl+p,ctrl+q的方式退出。



Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export WEBAPP_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/PegasusWang/flask-app
    cd flask-app
    pip install -r requirements/dev.txt
    bower install
    python manage.py server

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Deployment
----------

In your production environment, make sure the ``WEBAPP_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.

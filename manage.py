#!/usr/bin/python3
# -*- encoding:utf-8 -*-

from flask_script import Manager
from app import app
from db_script import DBManager
from flask_migrate import Migrate, MigrateCommand
from exts import db

manager = Manager(app)
# 1.使用flask-migrate必须绑定app和db
migrate = Migrate(app, db)
# 2.把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)

#命令：　init->migrate->upgrade

@manager.command
def runserver():
    return '服务器跑起来了...'


# 数据库
# manager.add_command('db', DBManager)

if __name__ == '__main__':
    manager.run()

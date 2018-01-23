#!/usr/bin/python3
# -*-encoding:utf-8-*-

from flask_script import Manager

DBManager = Manager()


@DBManager.command
def init():
    print('db init success')


@DBManager.command
def migrate():
    print('migrate db success')

#!/usr/bin/python3
# -*-encoding:utf-8-*-

from exts import db


class User(db.Model):
    __table_name__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String('100'), nullable=False)
    password = db.Column(db.String('100'), nullable=False)
    age = db.Column(db.Integer)


class Book(db.Model):
    __table_name__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(255), nullable=False)
    book_url = db.Column(db.String(200), nullable=False)
    book_author = db.Column(db.String(50), nullable=False)
    book_cover_url = db.Column(db.String(200))
    book_describe = db.Column(db.Text)
    type_id = db.Column(db.Integer, db.ForeignKey("book_type.id"))
    # 反向查询
    type = db.relationship('BookType', backref=db.backref('books'))


class BookType(db.Model):
    __table_name__ = 'book_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

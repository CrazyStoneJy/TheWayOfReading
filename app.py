# !/usr/bin/python3
# -*- encoding:utf-8 -*-

from flask import Flask, url_for, redirect, render_template
import config
from exts import db
from models import User, Book, BookType
from config import *

app = Flask(__name__)
app.config.from_object(config)

index = config.API_VERSION + "/index/"
db.init_app(app)

# 待app初始化完成（这块不太懂）
with app.app_context():
    db.create_all()


@app.route(index)
def index():
    return 'index'


@app.route('/')
def hello():
    # user = User.query.filter(User.username == 'jianyan').first()
    # print(user)
    # print(user.username)
    # print(user.password)

    # book_type = BookType.query.filter(BookType.id == 1).first()
    # print(book_type.id)
    # print(book_type.name)
    # books = book_type.books
    # for book in books:
    #     print(book.book_name)

    # print(book_type)
    # book = Book.query.filter(Book.book_name == "java编程思想").first()
    # print(book)
    # print(book.type.id)
    cards = []
    for i in range(20):
        card = dict()
        card['url'] = 'http://imgsrc.baidu.com/imgad/pic/item/6a63f6246b600c33fb7329e1114c510fd9f9a195.jpg'
        card['name'] = 'pic' + str(i)
        card['author'] = 'author' + str(i)
        cards.append(card)

    return render_template('index.html', cards=cards)


@app.route('/test/')
def test():
    return 'test'


@app.route('/redirect/')
def redirectTest():
    test_url = url_for('test')
    return redirect(test_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

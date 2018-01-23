# true enable debug mode,else false
DEBUG = True

# mysql config
DIALECT = 'mysql'
DRIVER = 'pymysql'
USER_NAME = 'root'
PASSWORD = '1992'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'reading'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USER_NAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# restful api version name
API_VERSION = '/v1'

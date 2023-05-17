from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#设置flask 关联的数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#数据库关联flask
db = SQLAlchemy(app)

#一个类表示一张表
class User(db.Model):
    #每个类，表示这个表的表头数量
    #id，username,email
    #在db,Column实例时说明当前这一列数据的配置
    # Integer 整形，primary_key设置主键
    id = db.Column(db.Integer, primary_key=True)
    #字符串类型，unique 为True代表这一列数据，是不是唯一
    #如手机号、邮箱的设定，nullable表示是否 可以为空
    #如果nullable为False，代表当前的字段为空
    username = db.Column(db.String(80), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email
    # 魔法方法，打印的时候使用 print log
    def __repr__(self):
        return '<User %r>' % self.username

if __name__=='__main__':
        db.create_all()

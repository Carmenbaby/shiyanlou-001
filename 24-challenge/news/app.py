import os
import json
from flask import Flask
from flask import render_template
from flask import abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name = name

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(89))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)

    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示所有文章的标题（title）列表，此外每个标题都需要使用 `<a href=XXX></a>` 链接到对应的文章内容页面
    file_data = File.query.all()
    return render_template('index.html',file_data=file_data)

@app.route('/files/<file_id>')
def file(file_id):
    # file_id 为 File 表中的文章 ID
    # 需要显示 file_id  对应的文章内容、创建时间及类别信息（需要显示类别名称）
    # 如果指定 file_id 的文章不存在，则显示 404 错误页面
    fiel_data = File.query.filter_by(id=file_id).first()
    if fiel_data:
        return render_template('file.html',fiel_data = fiel_data)
    else:
        abort(404)

#404错误视图函数
@app.errorhandler(404)
def not_f(error):
    return render_template('404.html'), 404

if __name__ == '__main__':

    #创建表 
    '''
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    '''
    #运行
    app.run(debug=True,port=3000)
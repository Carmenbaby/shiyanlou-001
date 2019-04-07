from flask import Flask
from flask import render_template
from flask import abort
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    # 显示文章名称的列表
    # 也就是 /home/shiyanlou/files/ 目录下所有 json 文件中的 `title` 信息列表
    #"D://shiyanlou/23-challenge/files/"
    #获取所有是.json文件
    filename_list = list(filter(lambda filename: os.path.splitext(filename)[1] == '.json',os.listdir(files_dir)))
    filepwd_list = list(map(lambda file:os.path.join(files_dir,file),filename_list))
    #填全文件路径，并加载json文件取出title
    files_json = []
    for file in filepwd_list:
        with open(file) as fd:
            files_json.append(json.load(fd))

    return render_template('index.html',files_json=files_json)

@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面
    file_path = os.path.join(files_dir, filename)
    if os.path.exists(file_path):
        with open(file_path) as fd:
            return render_template('file.html',file_json = json.load(fd))
    else:
        abrot(404)

@app.errorhandler(404)
def not_f(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    #project_dir 项目目录地址 和 存放files文件目录地址
     #这种写法 directory = os.path.join(os.getcwd(), '..', 'files') 
    project_dir = os.path.dirname(os.path.dirname(__file__))  #linux 使用getcwd()

    app.run(debug=True,port=3000)
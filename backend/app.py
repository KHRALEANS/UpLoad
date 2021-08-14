from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Flask的跨域问题
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r"./upload"
CORS(app)  # Flask的跨域问题


#@app.route('/')
@app.route('/upload', methods=["POST"])  # 方法要与前端一致
def upload():
    file_obj = request.files['file']  # Flask中获取文件
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    # 保存文件
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "1.jpg")
    file_obj.save(file_path)
    return file_path


if __name__ == "__main__":
    app.run()

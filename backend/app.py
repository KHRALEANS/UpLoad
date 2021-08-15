from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Flask的跨域问题
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r"./uploaded"
CORS(app)  # Flask的跨域问题


# @app.route('/')
@app.route('/upload/zip', methods=["POST"])  # 上传zip
def uploadzip():
    file_obj = request.files['file']  # Flask中获取文件
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    # 保存文件
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "zip_files", "1.zip")
    file_obj.save(file_path)
    return file_path


@app.route('/upload/pdf', methods=["POST"])  # 上传pdf
def uploadpdf():
    file_obj = request.files['file']
    if file_obj is None:
        return "未上传文件"

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "pdf_files", "1.pdf")
    file_obj.save(file_path)
    return file_path


@app.route('/upload/txt', methods=["POST"])  # 上传txt
def uploadtxt():
    file_obj = request.files['file']
    if file_obj is None:
        return "未上传文件"

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "txt_files", "1.txt")
    file_obj.save(file_path)
    return file_path


@app.route('/upload/mp4', methods=["POST"])  # 上传mp4
def uploadmp4():
    file_obj = request.files['file']
    if file_obj is None:
        return "未上传文件"

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "mp4_files", "1.mp4")
    file_obj.save(file_path)
    return file_path


if __name__ == "__main__":
    app.run()

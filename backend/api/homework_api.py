import inject
from flask import request, jsonify, send_file, send_from_directory, make_response
from backend.models.homework_model import Homework
from backend.services.homework_service import HomeworkService
from backend.api import bp
import os

homework_service = inject.instance(HomeworkService)
UPLOAD_FOLDER = r"backend/uploaded"


def createPath(filePath):
    if os.path.exists(filePath):
        return False
    else:
        try:
            os.mkdir(filePath)
            return True
        except Exception as e:
            print(e)
            os.makedirs(filePath)
            return True


def makeFileName(fileId: str, fileName: str, studentName: str):
    file_name = fileName.split('.')
    origin_filename = file_name[0]
    newer_filename = studentName + '_' + origin_filename + '_' + fileId
    index = len(origin_filename)
    final_file_name =  newer_filename + fileName[index:]
    return final_file_name


@bp.route('/homeworks/<id>/files/<fileId>', methods=['GET'])
def download_file(id, fileId):
    file_name = request.args.get('fileName')
    student_name = request.args.get('studentName')

    homework_path = os.path.join(UPLOAD_FOLDER, student_name, id)
    final_file_name = makeFileName(fileId, file_name, student_name)

    return send_from_directory(homework_path, final_file_name, as_attachment=True)


@bp.route('/homeworks/<id>/files/<fileId>', methods=['POST'])
def upload_file(id, fileId):
    file_name = request.args.get('fileName')
    student_name = request.args.get('studentName')
    file_obj = request.files['file']  # Flask中获取文件
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    file_format = file_name.split('.')  # 格式检查
    if ('zip' in file_format) or ('pdf' in file_format) or ('txt' in file_format) or ('mp4' in file_format):
        # 符合格式
        student_path = os.path.join(UPLOAD_FOLDER, student_name)
        createPath(student_path)
        # 创建学生目录
        homework_path = os.path.join(student_path, id)
        createPath(homework_path)
        # 创建作业目录
        final_file_name = makeFileName(fileId, file_name, student_name)
        # 创建保存文件名
        file_path = os.path.join(homework_path, final_file_name)
        file_obj.save(file_path)
        # 保存文件
    else:
        return "格式不正确"

    result = {
        "filepath": file_path
    }

    return jsonify(result)

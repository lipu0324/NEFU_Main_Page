from django.http import HttpResponse
from django.shortcuts import render
from File_transfer.models import File_reg
from django import forms
from django.http import HttpResponse, Http404, FileResponse, StreamingHttpResponse
import os


# Create your views here.
def upload(request):
    if request.method == 'GET':
        return render(request, 'Upload.html')
    if request.method == 'POST':
        File = request.FILES.get('file', None)
        if File is None:
            return HttpResponse('No file')
        else:
            file_name = File.name
            file_path = './文件暂存地/' + file_name
            file_id = request.POST.get('file_code')
            # 数据存入数据库
            File_reg.objects.create(File_id=file_id, File_name=file_name, File_path=file_path)
            with open(file_path, 'wb') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            return HttpResponse('upload success')


# 这里返回一个迭代器,防止文件过大将内存打满,这样可以保证服务的占用内存几乎没有波动
def read_file(file_name, buf_size=409600):
    with open(file_name, "rb") as f:
        while True:
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break


def download(request):
    if request.method == 'GET':
        return render(request, 'download.html')
    if request.method == 'POST':
        file_code = request.POST.get('File_code', None)
        print(file_code)
        try:
            file_path = File_reg.objects.get(File_id=file_code).File_path
            file_name = File_reg.objects.get(File_id=file_code).File_name
        except File_reg.DoesNotExist:
            return HttpResponse('File not found')
        # 用户下载位于file_path的文件
        try:
            res = StreamingHttpResponse(read_file(file_path))
            # 增加headers
            res['steaming_content'] = "file_name"
            return res
        except FileNotFoundError:
            return HttpResponse('File not found')


def mainpage(request):
    return render(request, 'mainpage.html')

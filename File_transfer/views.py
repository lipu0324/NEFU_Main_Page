from django.http import HttpResponse
from django.shortcuts import render
from File_transfer.models import File_reg
from django import forms


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


def download(request):
    if request.method == 'GET':
        return render(request, 'download.html')
    # 创建一个字符串来接受文件提取码
    file_extract_code = request.POST.get('downloader')
    # print(file_extract_code)
    # 查询所有的可以下载的文件名称
    file_list = File_reg.objects.filter(Recieve_user=file_extract_code)
    print(file_list)
    return render(request, 'download.html', {'download_list': file_list})


def mainpage(request):
    return render(request, 'mainpage.html')

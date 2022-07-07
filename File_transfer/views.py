from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from File_transfer.models import File_reg

# Create your views here.
def upload(request):

    if request.method == 'POST':
        #打印接收者
        print(request.POST.get('receive'))
        # 获取上传文件，如果没有上传文件，则默认为None
        upload_file = request.FILES.get('file', None)
        if not upload_file:
            return HttpResponse('请选择上传文件')
        # 创建文件，保存文件
        with open('E:/编程项目主文件夹/nefu_start_page_manager/文件暂存地/' + upload_file.name, 'wb+') as f:
            for chunk in upload_file.chunks():
                f.write(chunk)
        # 将文件信息保存到数据库
        File_reg.objects.create(File_name=upload_file.name, File_path='E:/编程项目主文件夹/nefu_start_page_manager/文件暂存地' + upload_file.name, Upload_time=datetime.now(), Upload_user=request.POST.get('sender'), Recieve_user=request.POST.get('receive'), Encryption_status=False)
        return HttpResponse('上传成功')
    return render(request, 'Upload.html')

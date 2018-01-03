# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from models.models import Photo
from models import photoDao
import random

# 随机获取两张图片
def getPhotos():
    # 数据库中所有图片
    list = Photo.objects.all()
    size = len(list) - 1

    # 生成一个随机数
    tmp = random.randint(0, size)
    src1 = list[tmp].content
    id1 = list[tmp].id

    # 生成另一个随机数
    tmp2 = random.randint(0, size)
    while tmp2 == tmp:
        tmp2 = random.randint(0, size)

    src2 = list[tmp2].content
    id2 = list[tmp2].id

    context = {}
    context['src1'] = src1
    context['src2'] = src2
    context['id1'] = id1
    context['id2'] = id2
    return context

# 加载初始化页面
def index(request):
    context = getPhotos()
    return render(request, 'index.html', context)


# 用户点击选择自己喜欢的照片
def chooseFavor(request):
    favorPhoto_Id = request.POST['favorPhoto']
    # 给对应的照片被喜欢次数加1
    photoDao.addFavorNum(favorPhoto_Id)
    # 加载新的照片
    return redirect('/')

# 照片列表
def list(request):
    # 数据库中所有图片
    list = Photo.objects.all().order_by('-favorNum')
    context = {}
    context['photolist'] = list
    return render(request, 'list.html', context)

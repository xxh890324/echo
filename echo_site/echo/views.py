# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Node

def lists(request):
	#从node获取所有数据
	data = Node.objects.all()
	#建立context字典，将值传递给对应页面
	context = {'data':data,}
	#跳转到对应页面，并传递值
	return render(request,'lists.html',context)


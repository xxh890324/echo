# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Node,Server,Device
from forms import NodeForm,ServerForm,DeviceForm
from django.shortcuts import render,redirect

def lists(request):
	#从node获取所有数据
	data = Node.objects.all()
	#建立context字典，将值传递给对应页面
	context = {'data':data,}
	#跳转到对应页面，并传递值
	return render(request,'lists.html',context)


def add(request):
	#获取nodeform表单数据
	form = NodeForm(request.POST or None)
	#判断form是否有效
	if form.is_valid():
		#创建实例，需要做数据处理，暂时不保存
		instance = form.save(commit=False)
		#将登陆用户作为登记人
		instance.node_signer = request.user
		#保存实例
		instance.save()
		#跳转页面
		return redirect('/lists')

	#创建context集中处理需要传递到页面的数据
	context = {'form':form,}

	#如果没有有效提交，则停留在原来页面
	return render(request,'add.html',context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Node(models.Model):

	type = (
		(U'基层法院','基层法院'),
		(U'中级法院','中级法院'),
		(U'高级法院','高级法院'),
	)

	node_name = models.CharField(verbose_name='节点名称',max_length=255)
	node_type = models.CharField(verbose_name='节点类型',max_length=100,choices=type)
	node_address = models.CharField(verbose_name='节点地址',max_length=255)
	node_contact = models.CharField(verbose_name='节点联系人',max_length=255,blank=True)
	node_signer = models.CharField(verbose_name='登记人',max_length=50,default='system')
	node_remarks = models.CharField(verbose_name='备注',max_length=255,blank=True)
	node_signtime = models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.node_name

class Server(models.Model):

	node = models.ForeignKey(Node,on_delete=models.PROTECT)

	#服务器用途分类
	sertype = (
		(u'业务服务器','业务服务器'),
		(u'平台服务器','平台服务器'),
		(u'画面合成服务器','画面合成服务器'),
		(u'数据库服务器','数据库服务器'),
		(u'中间件服务器','中间件服务器'),
		(u'其他','其他')
	)

	server_code = models.CharField(verbose_name='服务器编号',max_length=100)
	server_local = models.CharField(verbose_name='所在节点',max_length=100)
	server_sertype = models.CharField(verbose_name='服务器类型',max_length=100,choices=sertype)
	server_ip = models.CharField(verbose_name='服务器IP地址',max_length=100)
	server_signer = models.CharField(verbose_name='登记人',max_length=100,default='system')
	server_signtime = models.DateField(auto_now_add=True)
	server_remarks = models.CharField(verbose_name='备注',max_length=255,blank=True)

	def __unicode__(self):
		return self.server_code

class Device(models.Model):

	node = models.ForeignKey(Node,on_delete=models.PROTECT)

	devtype = (
		(u'摄像机','摄像机'),
		(u'编码器','编码器'),
		(u'解码器','解码器'),
		(u'其他','其他'),
	)

	device_name = models.CharField(verbose_name='设备名称',max_length=255)
	device_ip = models.CharField(verbose_name='设备IP',max_length=100)
	device_devtype = models.CharField(verbose_name='设备类型',max_length=200,choices=devtype)
	device_vendor = models.CharField(verbose_name='设备厂商',max_length=100)
	device_signer = models.CharField(verbose_name='登记人',max_length=100,default='system')
	device_signtime = models.DateField(auto_now_add=True)
	device_remarks = models.CharField(verbose_name='备注',max_length=255,blank=True)

	def __unicode__(self):
		return self.device_name

# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Node,Server,Device

#定义node的Form，Form的名字为模式名+Form
class NodeForm(ModelForm):
	#自定义ModelForm的内容
	class Meta:
		#modelform参照Model：Node
		model = Node
		exclude = ['node_signer']

class ServerForm(ModelForm):
	class Meta:
		model = Server
		exclude = ['server_signer']

class DeviceForm(ModelForm):
	class Meta:
		model = Device
		exclude = ['device_signer']

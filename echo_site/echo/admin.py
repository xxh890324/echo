# -*- coding: utf-8 -*-
from django.contrib import admin

#注册模块
from .models import Node,Server,Device

class NodeAdmin(admin.ModelAdmin):
    list_display = ('node_name','node_address','node_signer')
    exclude = ['node_signer']

    def save_model(self,request,obj,form,change):
        obj.node_signer = str(request.user)
        obj.save()

admin.site.register(Node,NodeAdmin)

class ServerAdmin(admin.ModelAdmin):
    list_display = ('server_ip','server_sertype','server_local','server_signer','server_remarks')
    exclude = ('server_signer',)
    def save_model(self,request,obj,form,change):
        obj.server_signer = str(request.user)
        obj.save()

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name','device_ip','device_devtype','device_vendor','device_signer','device_remarks')
    exclude = ('device_signer',)
    def save_model(self,request,obj,form,change):
        obj.device_signer = str(request.user)
        obj.save()

admin.site.register(Server,ServerAdmin)
admin.site.register(Device,DeviceAdmin)

# -*- coding: utf-8 -*-
from django.contrib import admin

#注册模块
from .models import Node

class NodeAdmin(admin.ModelAdmin):
    list_display = ('node_name','node_address','node_signer')
    exclude = ['node_signer']

    def save_model(self,request,obj,form,change):
        obj.node_signer = str(request.user)
        obj.save()

admin.site.register(Node,NodeAdmin)

#!/usr/bin/python
# -*- coding: utf-8 -*-

#  _   _       _ _                     _
# | | | | ___ | | |__  _ __ ___   ___ | | __
# | |_| |/ _ \| | '_ \| '__/ _ \ / _ \| |/ /
# |  _  | (_) | | |_) | | | (_) | (_) |   <
# |_| |_|\___/|_|_.__/|_|  \___/ \___/|_|\_\
# wanghaikuo@gmail.com


from django.db import models
from mptt.models import MPTTModel

class BizCategory(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'类别名称')
    #parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'业务类别'
        verbose_name_plural = u'业务类别'
        #app_label = u"我的应用"

class BizLevel(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'名称')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'业务级别'
        verbose_name_plural = u'业务级别'

class BizObject(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'名称')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)
    category = models.ForeignKey('BizCategory', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'业务对象'
        verbose_name_plural = u'业务对象'

class BizObjAttr(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'名称')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)
    obj = models.ForeignKey('BizObject', blank=True, null=True)
    attr_type = models.CharField(max_length=200,verbose_name=u'类型')
    length = models.CharField(max_length=200,verbose_name=u'长度',blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'业务对象属性'
        verbose_name_plural = u'业务属性'


class BizService(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'服务名称')
    category = models.ForeignKey('BizCategory', blank=True, null=True)
    level = models.ForeignKey('BizLevel', blank=True, null=True)
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)
    dependencies = models.ManyToManyField("self",blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'业务服务'
        verbose_name_plural = u'业务服务'



class Application(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'应用系统名称')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'应用系统'
        verbose_name_plural = u'应用系统'

class AppService(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'应用服务名称')
    app = models.ForeignKey('Application')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'应用服务'
        verbose_name_plural = u'应用服务'


class Protocol(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'通信协议名称')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)

    class Meta:
        verbose_name = u'通信协议'
        verbose_name_plural = u'通信协议'

class ExposeType(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'通信协议名称')


class AppInterface(models.Model):
    version = models.CharField(max_length=200,verbose_name=u'版本')



class DataProtocol(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'名称')
    version = models.CharField(max_length=200,verbose_name=u'版本')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)

    class Meta:
        verbose_name = u'数据交换协议'
        verbose_name_plural = u'数据交换协议'


class Message(models.Model):
    code = models.CharField(max_length=200,verbose_name=u'编码')
    name = models.CharField(max_length=200,verbose_name=u'名称')
    doc = models.TextField(verbose_name=u'说明',blank=True, null=True)

    class Meta:
        verbose_name = u'消息/报文'
        verbose_name_plural = u'消息/报文'

class Field(models.Model):
    code = models.CharField(max_length=200,verbose_name=u'编码')
    name = models.CharField(max_length=200,verbose_name=u'名称')
    field_type = models.CharField(max_length=200,verbose_name=u'类型')

    parent = models.ForeignKey('Message')

    class Meta:
        verbose_name = u'字段'
        verbose_name_plural = u'字段'


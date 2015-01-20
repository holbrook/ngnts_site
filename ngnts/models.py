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

class BizService(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'服务名称')
    category = models.ForeignKey('BizCategory')
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


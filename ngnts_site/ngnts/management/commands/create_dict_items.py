#!/usr/bin/python
# -*- coding: utf-8 -*-

#  _   _       _ _                     _
# | | | | ___ | | |__  _ __ ___   ___ | | __
# | |_| |/ _ \| | '_ \| '__/ _ \ / _ \| |/ /
# |  _  | (_) | | |_) | | | (_) | (_) |   <
# |_| |_|\___/|_|_.__/|_|  \___/ \___/|_|\_\
# wanghaikuo@gmail.com

import os
import os.path

from django.core.management.base import BaseCommand
from django.conf import settings

from ngnts.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        biz_cat1 = BizCategory.objects.create(name=u'交易')
        biz_cat2 = BizCategory.objects.create(name=u'结算')
        biz_cat3 = BizCategory.objects.create(name=u'信息披露')
        biz_cat4 = BizCategory.objects.create(name=u'监管报送')
        biz_cat5 = BizCategory.objects.create(name=u'行业间')
        biz_cat6 = BizCategory.objects.create(name=u'客户')
        biz_cat7 = BizCategory.objects.create(name=u'其他')

        biz_level1 = BizLevel.objects.create(name=u'规划')
        biz_level2 = BizLevel.objects.create(name=u'控制')
        biz_level3 = BizLevel.objects.create(name=u'执行')

        BizService.objects.create(category=biz_cat1,name=u'证券交易')
        BizService.objects.create(category=biz_cat1,name=u'大宗交易')
        BizService.objects.create(category=biz_cat1,name=u'固定收益交易')
        BizService.objects.create(category=biz_cat1,name=u'期货交易')
        BizService.objects.create(category=biz_cat1,name=u'股转交易')
        BizService.objects.create(category=biz_cat1,name=u'转融通交易')

        BizService.objects.create(category=biz_cat2,name=u'证券结算')
        BizService.objects.create(category=biz_cat2,name=u'开放式基金结算')
        BizService.objects.create(category=biz_cat2,name=u'期货结算')
        BizService.objects.create(category=biz_cat2,name=u'结算支付')
        BizService.objects.create(category=biz_cat2,name=u'担保品管理')
        BizService.objects.create(category=biz_cat2,name=u'转融通')

        BizService.objects.create(category=biz_cat3,name=u'证券行情')
        BizService.objects.create(category=biz_cat3,name=u'期货行情')
        BizService.objects.create(category=biz_cat3,name=u'港股行情')

#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from .models import UserAddress, UserIntegrate


class UserIntegrateAdmin(object):
    list_display = ['user', 'integrate_time', 'source', 'expiry_day']


class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(object):
    list_display = ["phone", "district", "address"]

#xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserIntegrate, UserIntegrateAdmin)
#xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
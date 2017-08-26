# -*- coding: UTF-8 -*-
import itchat


def getFriends(remark_name=''):
    friend = itchat.search_friends(remarkName=remark_name)
    return friend


def getImpage(self):
    pass

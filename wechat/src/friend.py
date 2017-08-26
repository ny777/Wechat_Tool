# -*- coding: UTF-8 -*-
import itchat


def getFriends(name=''):
    friend = itchat.search_friends(name=name)
    return friend


def getImpage(self):
    pass


def getChatroom(name=''):
    room = itchat.search_chatrooms(name=name)
    return room

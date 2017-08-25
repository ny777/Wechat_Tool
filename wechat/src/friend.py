# -*- coding: UTF-8 -*-
import itchat


class Friends:
    def __init__(self):
        self.__friend = itchat.get_friends(update=True)[0:]

    def getFriends(self):
        return self.__friend

    def getImpage(self):
        pass



# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *
import time


def getResponse(msg):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '0073e80d714e460d98b7cf5c605cb812',
        'info': msg,
        'userid': 'ny',
    }
    r = requests.post(api_url, data=data).json()
    return r


@itchat.msg_register(TEXT, isFriendChat=False, isGroupChat=False, isMpChat=True)
def autoReplyForMP(msg):
    text = msg['Text']
    reply = getResponse(text)['text']
    time.sleep(0.2)
    return reply


@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=False, isMpChat=False)
def autoReplyForFriend(msg):
    text = msg['Text']
    reply = '我是自动回复机器人: ' + getResponse(text)['text']
    time.sleep(0.1)
    return reply


@itchat.msg_register(TEXT, isFriendChat=False, isGroupChat=True, isMpChat=False)
def autoReplyForGroup(msg):
    text = msg['Text']
    print msg
    # reply = '我是自动回复机器人: ' + getResponse(text)['text']
    # time.sleep(0.1)


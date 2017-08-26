# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *


def getResponse(msg):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '这里换成图灵机器人key',
        'info': msg,
        'userid': 'ny',
    }
    r = requests.post(api_url, data=data).json()
    return r


@itchat.msg_register(TEXT, isFriendChat=False, isMpChat=True)
def autoReplyForMP(msg):
    text = msg['Text']
    reply = getResponse(text)['text']
    return reply


@itchat.msg_register(TEXT, isFriendChat=True)
def autoReplyForFriend(msg):
    text = msg['Text']
    reply = '我是自动回复机器人: ' + getResponse(text)['text']
    return reply

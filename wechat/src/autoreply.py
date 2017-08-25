# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *


def getResponse(msg):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '0073e80d714e460d98b7cf5c605cb812',
        'info': msg,
        'userid': 'ny',
    }
    r = requests.post(api_url, data=data).json()
    return r


@itchat.msg_register(TEXT)
def autoReply(msg):
    reply = '制杖者ny: ' + getResponse(msg['Text'])['text']
    return reply

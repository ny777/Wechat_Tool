# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *


def getResponse(msg):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '',
        'info': msg,
        'userid': 'ny',
    }
    r = requests.post(api_url, data=data).json()
    return r


@itchat.msg_register(TEXT)
def autoReply(msg):
    reply = '制杖者ny: ' + getResponse(msg['Text'])['text']
    return reply

# -*- coding: UTF-8 -*-
import sys
import friend
import itchat
import threading
import autoreply  # 虽然没有使用，但是必须引用否则线程启动无法调用


def main():
    reload(sys)
    sys.setdefaultencoding('utf8')  # 虽然报红但是有用
    while True:
        command = raw_input("Command:")
        if 'exit' == command:
            print itchat.logout()['BaseResponse']['RawMsg']
            sys.exit()
        elif 'logout' == command:
            print itchat.logout()['BaseResponse']['RawMsg']
        elif 'login' == command:
            itchat.auto_login(hotReload=True)
        elif 'signin' == command:
            itchat.login()
        elif 'getfriend' == command:
            w = friend.Friends()
            pal = w.getFriends()
            print pal[0]
        elif 'autoreply' == command:
            t = threading.Thread(target=itchat.run)
            t.start()
        elif 'test' == command:
            msg = raw_input("Say:")
            reply = autoreply.getResponse(msg)
            print reply['text'].decode()
            print reply
        else:
            print 'Wrong Command, Try Again'


if __name__ == '__main__':
    main()

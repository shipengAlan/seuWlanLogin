#! /usr/bin/env python
# coding = utf-8
#  Author:Shi Peng (shipeng.alan@gmail.com)
import requests
import json


class seuLogout(object):

    """docstring for seuLogout
    """

    def __init__(self):
        pass

    def post(self):
        url = "https://w.seu.edu.cn/portal/logout.php"
        r = requests.post(url)
        info = r.text
        info = info.split('\n')[1]
        state_info = json.loads(info)
        if state_info.has_key('error'):
            print state_info['error']
            print "Maybe Not Login"
            return False
        else:
            try:
                print 'Logint state:', state_info['success']
                print 'Location:', state_info['login_location']
                print 'IP:', state_info['login_ip']
                return True
            except:
                print "Logout Error"
                return False

if __name__ == "__main__":
    s = seuLogout()
    s.post()

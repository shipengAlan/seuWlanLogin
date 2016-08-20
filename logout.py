#! /usr/bin/env python
# coding : utf-8
# Author:Shi Peng (shipeng.alan@gmail.com)
import urllib
import json
import ConfigParser


class seuLogin(object):

    """docstring for seuLogin"""

    def __init__(self, username, pwd):
        super(seuLogin, self).__init__()
        self.username = username
        self.password = pwd

    def checkLogin(self):
        url = "http://w.seu.edu.cn/index.php/index/init"
        res = urllib.urlopen(url)
        info = res.read()
        # remove bom header
        state_info = json.loads(info)
        if state_info['status'] == 1:
            return True
        else:
            return False

    # no need cookie
    def Logout(self):
        url = "http://w.seu.edu.cn/index.php/index/logout"
        res = urllib.urlopen(url)
        info = res.read()
        # remove bom header
        state_info = json.loads(info)
        print 'Login info:', state_info['info']
        if state_info['status'] == 1:
            return True
        else:
            return False

    def Login(self):
        if self.checkLogin():
            self.Logout()

if __name__ == "__main__":
    cf = ConfigParser.ConfigParser()
    cf.read("account.conf")
    username = cf.get("account", "username")
    password = cf.get("account", "password")
    print username, password
    s = seuLogin(username, password)
    s.Login()

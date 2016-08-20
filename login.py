#! /usr/bin/env python
# coding : utf-8
# Author:Shi Peng (shipeng.alan@gmail.com)
import urllib2
import urllib
import json
import cookielib
import ConfigParser
import base64


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
            print 'Login info:', state_info['info']
            print 'Location:', state_info['logout_location']
            print 'Username:', state_info['logout_username']
            print 'IP:', state_info['logout_ip']
            return True
        else:
            return False

    # no need cookie
    def postWithCookie(self):
        cookiefile = "cookiefile"
        data = {'username': self.username,
                'domain': 'teacher',
                'password': base64.b64encode(self.password),
                'enablemacauth': 0
                }
        url = "https://w.seu.edu.cn/index.php/index/login"
        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        # user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
        # headers = {'User-Agent': user_agent}
        # enable cookie
        cookieJar = cookielib.MozillaCookieJar(cookiefile)
        cookieJar.save()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        urllib2.install_opener(opener)
        response = opener.open(req, data)
        cookieJar.save()
        # req = urllib2.Request(url, data, headers)
        # response = urllib2.urlopen(req)
        the_page = response.read()
        state_info = json.loads(the_page.strip('\n'))
        if state_info['status'] == 1:
            print 'Login info:', state_info['info']
            print 'Location:', state_info['logout_location']
            print 'Username:', state_info['logout_username']
            print 'IP:', state_info['logout_ip']
            return True
        else:
            return False

    def Login(self):
        if not self.checkLogin():
            self.postWithCookie()

if __name__ == "__main__":
    cf = ConfigParser.ConfigParser()
    cf.read("account.conf")
    username = cf.get("account", "username")
    password = cf.get("account", "password")
    print username, password
    s = seuLogin(username, password)
    s.Login()

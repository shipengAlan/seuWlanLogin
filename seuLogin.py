#! /usr/bin/env python
# coding : utf-8
# Author:Shi Peng (shipeng.alan@gmail.com)
import urllib2
import urllib
import json
import cookielib
import ConfigParser


class seuLogin(object):

    """docstring for seuLogin"""

    def __init__(self, username, pwd):
        super(seuLogin, self).__init__()
        self.username = username
        self.password = pwd

    def post(self):
        data = {'username': self.username,
                'password': self.password,
                }
        url = "https://w.seu.edu.cn/portal/login.php"
        data = urllib.urlencode(data)
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        state_info = json.loads(the_page.strip('\n').split('\n')[1])
        if state_info.has_key('error'):
            print state_info['error']
            return False
        else:
            try:
                print 'Logint state:', state_info['success']
                print 'Location:', state_info['login_location']
                print 'Username:', state_info['login_username']
                print 'IP:', state_info['login_ip']
                print 'Index:', state_info['login_index']
                return True
            except:
                print "Sorry, error: please check your account's authority to login"
                print "https://nic.seu.edu.cn"
                return False

    def checkLogin(self):
        url = "https://w.seu.edu.cn/portal/init.php"
        res = urllib.urlopen(url)
        info = res.read()
        # remove bom header
        info = info[3:]
        info_dict = json.loads(info)
        if info_dict.has_key('notlogin'):
            return False
        else:
            try:
                print 'Logint state:', "Have Logined"
                print 'Location:', info_dict['login_location']
                print 'Username:', info_dict['login_username']
                print 'IP:', info_dict['login_ip']
                print 'Index:', info_dict['login_index']
                return True
            except:
                print "Sorry, error: please check your account's authority to login"
                print "https://nic.seu.edu.cn"
                return False

    # no need cookie
    def postWithCookie(self):
        cookiefile = "cookiefile"
        url = "https://w.seu.edu.cn/portal/login.php"
        """
        cookieJar = cookielib.MozillaCookieJar(cookiefile)
        cookieJar.load(ignore_discard=True,ignore_expires=True)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
        url2 = "https://w.seu.edu.cn/portal/logout.php"
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url2)
        print response.read()
        return
        """
        data = {'username': self.username,
                'password': self.password,
                }
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
        print the_page
        state_info = json.loads(the_page.strip('\n').split('\n')[1])
        if state_info.has_key('error'):
            print state_info['error']
            return False
        else:
            print 'Logint state:', state_info['success']
            print 'Location:', state_info['login_location']
            print 'Username:', state_info['login_username']
            print 'IP:', state_info['login_ip']
            print 'Index:', state_info['login_index']
            return True

    def Login(self):
        if not self.checkLogin():
            self.post()

if __name__ == "__main__":
    cf = ConfigParser.ConfigParser()
    cf.read("account.conf")
    username = cf.get("account", "username")
    password = cf.get("account", "password")
    print username, password
    s = seuLogin(username, password)
    # print s.postWithCookie()
    s.Login()

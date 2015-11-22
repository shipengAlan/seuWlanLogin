#! /usr/bin/env python
# coding = utf-8
import urllib2
import urllib
import json


class seuLogout(object):

    """docstring for seuLogout
    """

    def __init__(self):
        pass

    def post(self):
        url = "https://w.seu.edu.cn/portal/logout.php"
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
        # headers = {'User-Agent': user_agent}
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
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

if __name__ == "__main__":
    s = seuLogout()  # "220151496", "200012shi"
    print s.post()

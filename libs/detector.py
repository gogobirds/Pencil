#!/usr/bin/env python
# coding : utf-8 
# author : 'Zend'
# team   : "gogobirds"


from plugins.base import pluginmap, load_plugins
from argparser import args


class Detector(object):
    def __init__(self):
        self.args = args
        self.plugins = pluginmap
        load_plugins()

    def detect(self, info):
        for item in self.plugins:
            pluginmap[item](args) if item[0] == info["app_name"] and item[1] == info["version"] else None






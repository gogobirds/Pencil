#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

from utils.http import request

SEARCHER = ("www.google.com", "www.baidu.com", "www.sogou.com")

BAIDU_BASIC = "http://www.baidu.com/#ie=utf-8&wd="
SOGOU_BASIC = "http://www.sogou.com/web?ie=utf-8&query="
GOOGLE_BASIC = "http://www.google.com/search?q="


class Searcher(object):
    def __init__(self, name, pattern, types="inurl"):
        self.name = name
        self.pattern = pattern
        self.types = types
        self.base_url = ""

    def set_searcher(self):
        switcher = {
            "baidu": "http://www.baidu.com/#ie=utf-8&wd=",
            "sogou": "http://www.sogou.com/web?ie=utf-8&query=",
            "google": "http://www.google.com/search?q=",
        }
        self.base_url = switcher.get(self.name, "nothing")

    def set_types(self):
        self.base_url += self.types + ":"

    def set_pattern(self):
        self.base_url += self.pattern

    def init_searcher(self):
        self.set_searcher()
        self.set_types()
        self.set_pattern()

    def get_searcher(self):
        return {
            "search_name": self.name,
            "search_types": self.types,
            "search_pattern": self.pattern,
            "search_url": self.base_url,
        }

    def run(self):
        return request(self.base_url)







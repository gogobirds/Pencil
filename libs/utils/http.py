#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

import requests


def request(url):
    r = requests.get(url)
    print r.encoding
    return r.text

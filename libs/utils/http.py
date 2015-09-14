#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

import requests
from url import normalize_url


def request(url):
    url = normalize_url(url)
    r = requests.get(url)
    return r

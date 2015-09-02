__author__ = 'Zend'

import requests


def request(url):
    r = requests.get(url)
    print r.encoding
    return r.text

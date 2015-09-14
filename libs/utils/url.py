#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

import socket
import urlparse

def normalize_url(url, https=False):
    if not url:
        return
    elif url.startswith(('http://', 'https://')):
        return url
    if not https:
        url = 'http://' + url
    else:
        url = 'https://' + url
    return url


def resolve_url(url):
    return socket.gethostbyname(urlparse.urlparse(url).netloc)

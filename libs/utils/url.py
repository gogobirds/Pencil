__author__ = 'MKT1'

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
    pass
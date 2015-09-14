#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

import nmap
nm = nmap.PortScanner()
nm.scan('222.197.183.136', '22-1000')
print nm.scaninfo()

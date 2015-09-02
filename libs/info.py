__author__ = 'Zend'

import nmap
nm = nmap.PortScanner()
nm.scan('222.197.183.136', '22-1000')
print nm.scaninfo()
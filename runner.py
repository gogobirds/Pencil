#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

from libs.cmd import args
from libs.searcher import Searcher

searcher = Searcher("baidu", "/index.php?m=menber&c=index&a=login")
searcher.init_searcher()
print searcher.get_searcher()
print searcher.run()

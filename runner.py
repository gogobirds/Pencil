#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

from libs.detector import Detector
from libs.printer import logger

# searcher = Searcher("baidu", "/index.php?m=menber&c=index&a=login")
# searcher.init_searcher()
# print searcher.get_searcher()
# print searcher.run()

logger.info("the scanner is starting")
detector = Detector()
detector.detect({"app_name": "www", "version": "0.1"})

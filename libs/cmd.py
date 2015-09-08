#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

import argparse

ArgumentParser = argparse.ArgumentParser(description="Web Scanner")

ArgumentParser.add_argument("-u", "--url", help="the url you want to scanner")
ArgumentParser.add_argument("-p", "--pattern", help="the parttern you want to scanner")
ArgumentParser.add_argument("-s", "--searcher", help="the ")

args = ArgumentParser.parse_args()


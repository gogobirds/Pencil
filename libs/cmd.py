__author__ = 'Zend'

import argparse

ArgumentParser = argparse.ArgumentParser(description="Web Scanner")

ArgumentParser.add_argument("-u", "--url", help="the url you want to scanner")
ArgumentParser.add_argument("-p", "--pattern", help="the parttern you want to scanner")
ArgumentParser.add_argument("-s", "--searcher", help="the ")

args = ArgumentParser.parse_args()


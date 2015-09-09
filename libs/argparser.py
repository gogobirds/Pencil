#!/usr/bin/env python
# coding : utf-8
# author : 'Zend'
# team   : "gogobirds"

import argparse


def base_parser():
    parser = argparse.ArgumentParser(description="Pencil Web Scanner")

    parser.add_argument("-u", "--url", help="the url you want to scanner")
    parser.add_argument("-p", "--pattern", help="the parttern you want to scanner")
    parser.add_argument("-s", "--searcher", help="the ")

    return parser.parse_args()


def user_parser():
    pass


args = base_parser()


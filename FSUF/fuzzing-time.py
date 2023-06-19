#!/usr/bin/env python3


from auxialiries.common_stuff import *
from bs4 import BeautifulSoup
from auxialiries.time import perf_counter
from auxialiries.ite import iterator
import argparse

put_together = []
def blah():
    parser = argparse.ArgumentParser()
    requiredArg = parser.add_argument_group('required arguments:')
    requiredArg.add_argument("-t", "-target", metavar="", required=True) 
    requiredArg.add_argument("-w", "-wordlist", metavar="", required=True)
    requiredArg.add_argument("-H", "-headers", required=True, metavar="", action="append", help="This is self explaining")
    requiredArg.add_argument("-d", "-data", metavar="", required=True, help="Do not set it for directory fuzzing mode")
    parser.add_argument("-x", "-proxy", metavar="", help="http://<ip>:<port>")
    parser.add_argument("-fr", "-filter-error", dest="filter_error", metavar="", help="Hide responses for given string")
    parser.add_argument("-fs", "-filter-size", dest="filter_size", metavar="", help="Hide responses by given size")
    args = parser.parse_args()
    headers = args.headers
    data = args.data
    target = args.target
    wordlist = args.wordlist
    proxy = args.proxy
    match_code = args.match_code
    filter_error = args.filter_error
    filter_size = args.filter_size
    if proxy is None:
        if data:
            iterator(target, headers, wordlist, data, proxies, match_code, filter_error, filter_size)
        else:
            print("NOT READY YET!! NOT SURE WHAT THIS IS FOR!")
    else:
        proxies = {"http": f"{proxy}"}
        if data:
            iterator(target, headers, wordlist, data, proxies, match_code, filter_error, filter_size)
        else:
            print("NOT READY YET!! ONLY POST REQUESTS SUPPORTED!")



blah()

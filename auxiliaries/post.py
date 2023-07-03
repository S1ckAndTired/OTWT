#!/usr/bin/env python3


from auxiliaries.common_stuff import *
from auxiliaries.requester import issuer
from urllib.parse import quote
def post_it(target, wordlist, body, proxies, filter_error, filter_size, delay):
    if "Content-Type" in custom_headers.keys():
        if "json" in custom_headers["Content-Type"] or "javascript" in custom_headers["Content-Type"]:
            f = open(wordlist, "r")
            for words in f:
                fuzz = words.strip()
                data = (f"{body.replace('FUZZ', fuzz)}")
                #print(data)
                issuer(target, data, fuzz, proxies, filter_error, filter_size, delay)
        elif "urlencoded" in custom_headers["Content-Type"]:
            f = open(wordlist, "r")
            for words in f:
                fuzz = words.strip()
                if "&" in fuzz:
                    fuzz = quote(fuzz)
                    data = body.replace("FUZZ", fuzz)
                    issuer(target, data, fuzz, proxies, filter_error, filter_size, delay)
                else:
                    data = body.replace("FUZZ", fuzz)
                    issuer(target, data, fuzz, proxies, filter_error, filter_size, delay)
        else:
            print("[-] OOPS!! Something else came up. Gotta implement it!!!")
    else:
        print("`[-] Content-Type` header is required")
    
    

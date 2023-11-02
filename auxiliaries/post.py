#!/usr/bin/env python3


from auxiliaries.common_stuff import *
from auxiliaries.requester import issuer
from auxiliaries.rate_limting import *
from urllib.parse import quote
def post_it(target, wordlist, body, proxies, filter_error, filter_size, delay, rate):
    if "Content-Type" in custom_headers.keys():
        if "json" in custom_headers["Content-Type"] or "javascript" in custom_headers["Content-Type"]:
            f = open(wordlist, "r")
            for words in f:
                last = words.strip().split()[-1]
                fuzz = words.strip()
                data = (f"{body.replace('FUZZ', fuzz)}")
                issuer(target, data, fuzz, proxies, filter_error, filter_size, delay, rate)
            last_worda.append(last)
        elif "urlencoded" in custom_headers["Content-Type"]:
            f = open(wordlist, "r")
            for words in f:
                last = words.strip().split()[-1]
                fuzz = words.strip()
                if "&" in fuzz:
                    fuzz = quote(fuzz)
                    data = body.replace("FUZZ", fuzz)
                    issuer(target, data, fuzz, proxies, filter_error, filter_size, delay, rate)
                else:
                    data = body.replace("FUZZ", fuzz)
                    issuer(target, data, fuzz, proxies, filter_error, filter_size, delay, rate)
            last_word.append(last)
            if last_word:
                time_slip(target, data, fuzz, proxies, filter_error, filter_size, delay, rate)
        else:
            print("[-] OOPS!! Something else came up. Gotta implement it!!!")
    else:
        print("`[-] Content-Type` header is required")
    
    

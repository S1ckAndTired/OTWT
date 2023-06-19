#!/usr/bin/env python3


from common_stuff import *
from requester import issuer
def post_it(target, wordlist, body, proxies, match_code, filter_error, filter_size):
    if "Content-Type" in custom_headers.keys():
        if "json" in custom_headers["Content-Type"] or "javascript" in custom_headers["Content-Type"]:
            if "&" in body:
                body = (str(f'"{body}"').replace("=", "\": \"").replace("&", "\", \""))
            else:
                body = (str(f'"{body}"').replace("=", "\": \""))
            f = open(wordlist, "r")
            for words in f:
                fuzz = words.strip()
                data = ("{"+f"{body.replace('FUZZ', fuzz)}"+"}")
                issuer(target, data, fuzz, proxies, match_code, filter_error, filter_size)
        elif "urlencoded" in custom_headers["Content-Type"]:
            f = open(wordlist, "r")
            for words in f:
                fuzz = words.strip()
                data = body.replace("FUZZ", fuzz)
                issuer(target, data, fuzz, proxies, match_code, filter_error, filter_size)
        else:
            print("[-] OOPS!! Something else came up. Gotta implement it!!!")
    else:
        print("`[-] Content-Type` header is required")
    
    

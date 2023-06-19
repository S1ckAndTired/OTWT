#!/usr/bin/env python3



from post import post_it
from common_stuff import *

def iterator(target, headers, wordlist, body, proxies, match_code, filter_error, filter_size):
    url = target
    for items in headers:
        param_name, param_value = items.split(": ")
        custom_headers[param_name] = param_value
    
    if "FUZZ" in body:
        post_it(target, wordlist, body, proxies, match_code, filter_error, filter_size)
    else:
         print("[-] Missing keyword `FUZZ`")

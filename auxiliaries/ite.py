#!/usr/bin/env python3



from auxiliaries.post import post_it
from auxiliaries.common_stuff import *

def iterator(target, headers, wordlist, body, proxies, filter_error, filter_size, delay):
    url = target
    for items in headers:
        param_name, param_value = items.split(": ")
        custom_headers[param_name] = param_value
    
    if "FUZZ" in body:
        post_it(target, wordlist, body, proxies, filter_error, filter_size, delay)
    else:
         print("[-] Missing keyword `FUZZ`")

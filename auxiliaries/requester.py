#!/usr/bin/env python3


from auxiliaries.common_stuff import *
from time import perf_counter
from time import sleep
import requests
import urllib3
urllib3.disable_warnings()



def issuer(target, body, fuzz, proxies, filter_error, filter_size, delay):
    start = perf_counter()
    r = requests.post(target, data=body, headers=custom_headers, proxies=proxies, verify=False)
    end = perf_counter()
    elapsed = end - start
    only_three = "{:.3f}".format(elapsed)
    if delay:
        sleep(int(delay))
    else:
        pass
    if filter_error is None and filter_size is None:
        print(f"[*] Elapsed-[{only_three}] Size-[{len(r.text)}] Code-[{r.status_code}] User-[{fuzz}]")
    elif filter_size:
        if str(len(r.text)) not in str(filter_size):
            print(f"[*] Elapsed-[{only_three}] Size-[{len(r.text)}] Code-[{r.status_code}] User-[{fuzz}]")
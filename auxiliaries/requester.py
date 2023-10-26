#!/usr/bin/env python3


from auxiliaries.common_stuff import *
from auxiliaries.rate_limting import *
from time import perf_counter
from time import sleep
from bs4 import BeautifulSoup
import requests
import re
from urllib3 import disable_warnings
disable_warnings()



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
    if str(filter_error) in r.text:
        print("[!] Rate limiting detected")
        if fuzz not in tmp_saver:
            tmp_saver.append(fuzz)
    else:
        if filter_error is None and filter_size is None:
            print(f"[*] Elapsed-[{only_three}] Size-[{len(r.text)}] Code-[{r.status_code}] Payload-[{fuzz}]")
        elif filter_size:
            if str(len(r.text)) not in str(filter_size):
                print(f"[*] Elapsed-[{only_three}] Size-[{len(r.text)}] Code-[{r.status_code}] Payload-[{fuzz}]")
        elif filter_error is not None:
            if str(filter_error) not in r.text:
                if filter_size:
                    if str(len(r.text)) not in str(filter_size):
                        print(f"[*] Elapsed-[{only_three}] Size-[{len(r.text)}] Code-[{r.status_code}] Payload-[{fuzz}]")
                else:
                    print(f"[*] Elapsed-[{only_three}] Size-[{len(r.text)}] Code-[{r.status_code}] Payload-[{fuzz}]")

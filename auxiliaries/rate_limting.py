#!/usr/bin/env python3

from bs4 import BeautifulSoup
from auxiliaries.common_stuff import *
from time import perf_counter
import requests
import re
from time import sleep



def time_slip(target, data, fuzz, proxies, filter_error, filter_size, delay, rate):    
    print(f"[*] Remaining requests gonna take 30 seconds each")
    for fuzx in tmp_saver:
        remaining_data = data.replace(last_word[0], fuzx)
        
        start = perf_counter()
        x = requests.post(target, data=remaining_data, headers=custom_headers, proxies=proxies, verify=False)
        end = perf_counter()
        elapsed = end - start
        only_three = "{:.3f}".format(elapsed)
        if filter_error is None and filter_size is None:
            print(f"[*] Elapsed-[{only_three}] Size-[{len(x.text)}] Code-[{x.status_code}] Payload-[{fuzx}]")
        elif filter_error is not None and filter_size is not None:
            if str(filter_error) not in x.text and str(len(x.text)) not in str(filter_size):
                print(f"[*] Elapsed-[{only_three}] Size-[{len(x.text)}] Code-[{x.status_code}] Payload-[{fuzx}]")
        elif filter_error is not None:
            print(f"[*] Elapsed-[{only_three}] Size-[{len(x.text)}] Code-[{x.status_code}] Payload-[{fuzx}]") 
        elif filter_size is not None:
            print(f"[*] Elapsed-[{only_three}] Size-[{len(x.text)}] Code-[{x.status_code}] Payload-[{fuzx}]")
        else:
            pass
        sleep(30)

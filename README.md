# OTWT - Only Time Will Tell ![Python minimum version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)

##### OTWT was created mainly and only for registration/login enumeration purposes. For now, it only accepts `POST` requests with either the `urlencoded` or `json` format.
_____________________________________________________________________________________________________________________
### Features
    Filter responses by response size
    Filter responses by given text in response (SOON!)

##### The ultimate feature is the `perf_counter()` add on. This simple thing, combined with `response size` allows you to determine existing/valid usernames when the `status_code` turned out to be the same for every request.

_____________________________________________________________________________________________________________________
:man_technologist: Usage

    usage: fuzzing-time.py [-h] -t  -w  -H  -d  [-x] [-fr] [-fs]

    optional arguments:
      -h, --help            show this help message and exit
      -x , -proxy           http://<ip>:<port>
      -fr , -filter-error   Hide responses for given string
      -fs , -filter-size    Hide responses by given size
    
    required arguments::
      -t , -target 
      -w , -wordlist 
      -H , -headers         This is self explaining
      -d , -data 

_____________________________________________________________________________________________________________________
##### Sure thing I will upgrade it so it supports `PUT` requests. In order to suply data `json` just suply it as `urlencoded` (e.g { "username": "admin" } - username=admin) 

##### :warning: Disclaimer! - Only use it under prior authorization of the target. I do not take any responsibility for its use. :warning:

    
    

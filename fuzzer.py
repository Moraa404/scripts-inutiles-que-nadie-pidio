#!/usr/bin/env python3
import requests
import argparse
import os
import concurrent.futures
from tqdm import tqdm

found_urls = 0

def print_success(v):
    print("\033[1;32m[+]" + "\033[0m", v)
def print_warning(v):
    print("\033[1;33m[!]" + "\033[0m", v)
def print_error(v):
    print("\033[1;31m[-]" + "\033[0m", v)

hp = argparse.ArgumentParser(description='Fuziing Tool by moraa404')
hp.add_argument('-u', '--url', type=str, help='URL 2 Test')
hp.add_argument('-w', '--wordlist', type=str, help='Wordlist to use')
hp.add_argument('-m', '--method', type=str, default='GET', help='Method to use ( GET / POST / PUT / DELETE / ... )')
hp.add_argument('-a', '--auth', type=str, default=None, help='Authentication type to use (HTTP basic / Digest / NTLM / ... )')
hp.add_argument('-x', '--ext', type=str, default='', help='File extension to search for (Default: no extension)')
hp.add_argument('-c', '--custom', type=str, default='', help='Custom string to add to the end of each path')
hp.add_argument('-t', '--threads', type=int, default=10, help='Number of threads to use')
hp.add_argument('-p', '--proxies', type=str, nargs='*', help='Proxys to use')
hp.add_argument('-H', '--header', type=str, nargs='*', help='Custom Headers')
args = hp.parse_args()

url = args.url.rstrip('/')
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url
wordlist = args.wordlist
if not os.path.isfile(wordlist):
    print_error(f'Cannot find file' + ' "' + wordlist + '"')
    exit()

with open(wordlist, 'r') as f:
    wordlist = f.read().splitlines()

method = args.method.upper()
auth = args.auth
ext = args.ext
custom = args.custom
threads = args.threads
proxies = {}
if args.proxies:
    proxies = {
    'http': args.proxies,
    'https': args.proxies
    }
headers = {}
if args.header:
    for header in args.header:
        if ':' in header:
            h = header.split(':')
            headers[h[0]] = h[1]

    print_success(f'Fuzzing in ' + str(url) +  ' using ' + str(method) + ' with ' + str(threads) + ' threads...')

def fuzz(path):
    full_url = f'{url}/{path}.{ext}{custom}' if ext else f'{url}/{path}{custom}'

    try:
        response = requests.request(method, full_url, auth=auth, proxies=proxies, headers=headers)

        if response.status_code == 200:
            print_success(full_url)
            found_urls =+ 1
        elif response.status_code == 401:
            print_warning(full_url + '\033[1;31m requires authentication' + '\033[0m')
            found_urls =+ 1
        elif response.status_code == 403:
            print_warning(full_url + '\033[1;33m is forbidden' + '\033[0m')
            found_urls =+ 1
    except requests.exceptions.RequestException as e:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor: 
       #results = list(tqdm(executor.map(fuzz, wordlist), total=len(wordlist), desc="progress"))
        results = list(executor.map(fuzz, wordlist), total=len(wordlist), desc="progress")

if found_urls:
    with open('results.txt', 'w') as file:
        for url in found_urls:
            f.write(url + '\n')
    print_success(f'Results saved in "results.txt"')
else:
    print("\n")
    print_warning('No results found')

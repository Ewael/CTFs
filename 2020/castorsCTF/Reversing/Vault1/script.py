#!/usr/bin/env python3

import base64
from pwn import xor

ch = "ExMcGQAABzohNQ0TRQwtPidYAS8gXg4kAkcYISwOUQYS"
ch = base64.b64decode(ch)
key = "promortyusvatofacidpromortyusvato"
res = xor(ch, key)

print(res)

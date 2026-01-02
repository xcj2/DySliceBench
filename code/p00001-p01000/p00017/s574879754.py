#!/usr/bin/env python
import sys
import re

def move(char, num):
    if ord(char) + num <= ord('z'):
        return ord(char) + num
    else:
        return ord(char) + num - (ord('z') - ord('a') + 1)

def shift(s, num):
    new = ""
    for i in range(0, len(s)):
        if s[i].isalpha():
            new += str(chr(move(s[i], num)));
        else:
            new += s[i]
    return new

def decrypt(s):
    for i in range(0, 26):
        decrypted = shift(s, i)
        if re.search('the|this|that', decrypted):
            return decrypted

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)
    for line in lines:
        print(decrypt(line), end="")
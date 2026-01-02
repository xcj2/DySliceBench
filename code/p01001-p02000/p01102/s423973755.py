#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def rdp_connect() -> bool:
    global s1, s2
    s1 = input()
    if s1 == '.':
        return False
    s2 = input()
    return True

def rdp_token(s: str):
    res = []
    while s:
        match = re.match(r'[a-zA-Z0-9;]+', s)
        if match:
            res.append(s[:match.end()])
            s = s[match.end():]
            continue
        match = re.match(r'"[^"]*"', s)
        if match:
            res.append(s[:match.end()-1])
            s = s[match.end():]
            continue
        break
    return res

def rdp_check() -> bool:
    l1 = rdp_token(s1)
    l2 = rdp_token(s2)
    if len(l1) != len(l2):
        return False
    flag = True
    for t1, t2 in zip(l1, l2):
        if t1 == t2:
            continue
        if t1[0] == t2[0] == '"' and flag:
            flag = False
        else:
            return False
    return True

if __name__ == '__main__':
    while rdp_connect():
        if s1 == s2:
            print('IDENTICAL')
        elif rdp_check():
            print('CLOSE')
        else:
            print('DIFFERENT')
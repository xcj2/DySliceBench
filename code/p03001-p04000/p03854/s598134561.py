import numpy as np
import math
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

s = list(input())
s.reverse()
v = []
v.append(list("dream"))
v.append(list("erase"))
v.append(list("eraser"))
v.append(list("dreamer"))
for i in range(4):
    v[i].reverse()

now = 0
while(1):
    check = False
    for i in range(4):
        if now+len(v[i]) > len(s): continue
        tmp = ''.join(s[now:now+len(v[i])])
        x = ''.join(v[i])
        if tmp == x:
            check = True
            now += len(v[i])
        if check: break
    if not check: break
    if now == len(s): break

if check: print("YES")
else: print("NO")
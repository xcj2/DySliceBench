import numpy as np
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

s = input()
ans = 0
for i in range(1<<(len(s)-1)):
    tmp = int(s[0])
    for j in range(len(s)-1):
        if i & 1<<j:
            ans += tmp
            tmp = int(s[j+1])
        else:
            tmp = tmp*10 + int(s[j+1])
    ans += tmp
print(ans)
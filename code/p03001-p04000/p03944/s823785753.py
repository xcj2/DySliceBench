import numpy as np
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

w, h, n = imap()
x = [0]*n; y = [0]*n; a = [0]*n
for i in range(n):
    x[i], y[i], a[i] = imap()

xr = yu = 0
xl = w; yd = h
for i in range(n):
    if a[i]==1: xr = max(xr, x[i])
    if a[i]==2: xl = min(xl, x[i])
    if a[i]==3: yu = max(yu, y[i])
    if a[i]==4: yd = min(yd, y[i])
sx = min(w, xr+w-xl)
sy = min(h, yu+h-yd)
print(h*w-(sx*h+sy*w-sx*sy))
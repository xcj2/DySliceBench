import sys
import math
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def s():return str(sys.stdin.readline().replace("\n",""))
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def strl():return [str(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx():return list(map(lambda x:int(x)*-1,sys.stdin.readline().replace("\n","").split()))
def t():return tuple(map(int,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":pass
n = i()
a = intl()
A = list(set(a))
d = {}
c = 0
def f(c):
    return (c*(c-1))//2
for i in range(n):
    try:
        d[a[i]] += 1
    except KeyError:
        d[a[i]] = 1
for i in A:
    c += f(d[i])
for i in range(n):
    t = d[a[i]]
    if t > 1:
        print(c-t+1)
    else:
        print(c)
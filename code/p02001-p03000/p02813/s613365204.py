import sys
import math
import itertools as it
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def s():return str(sys.stdin.readline().replace("\n",""))
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx():return list(map(lambda x:int(x)*-1,sys.stdin.readline().replace("\n","").split()))
def t():return tuple(map(int,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":pass

n = i()
p = t()
q = t()
pt = 1
ck = 0
l = [i for i in range(1,n+1)]
for i in it.permutations(l):
    if p == i:
        cnt1 = pt
        ck += 1
    elif i == q:
        cnt2 = pt
        ck += 1
    pt += 1
if ck >= 2:
    print(abs(cnt1-cnt2))
else:
    print(0)
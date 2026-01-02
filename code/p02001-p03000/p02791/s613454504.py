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
p = intl()
cnt = 0
m = p[0]
for i in range(n):
    if m > p[i]:
        m = p[i]
    if p[i] <= m:
        cnt += 1
print(cnt)
import sys
import math
def i():return int(sys.stdin.readline().replace("\n",""))
def i2():return map(int,sys.stdin.readline().replace("\n","").split())
def s():return str(sys.stdin.readline().replace("\n",""))
def l():return list(sys.stdin.readline().replace("\n",""))
def intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def lx():return list(map(lambda x:int(x)*-1,sys.stdin.readline().replace("\n","").split()))
def t():return tuple(map(int,sys.stdin.readline().replace("\n","").split()))

if __name__ == "__main__":pass
n,m,c = i2()
b = intl()
cnt = 0
s = 0
for i in range(n):
    a = intl()
    for i in range(m):
        s += a[i]*b[i]
    if s+c > 0:
        cnt += 1
    s = 0
print(cnt)
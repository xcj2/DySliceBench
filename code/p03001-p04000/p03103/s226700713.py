import sys
import math
import itertools
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

n, m = I2()
a = [Intl() for i in range(n)]
a.sort()
i = 0#index
c = 0#コスト
s = 0#本数累積和
while s < m:
    s += a[i][1]
    c += a[i][0]*a[i][1]
    i += 1
i -= 1

print(c-a[i][0]*(s-m))
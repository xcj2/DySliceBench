import sys
import math
import itertools
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

n = I()
s = [S() for i in range(n)]
m = I()
t = [S() for i in range(m)]
ans,cnt = 0,0
for i in s:
    cnt = 0
    l = [k for k,x in enumerate(s) if x == i]
    cnt += len(l)
    l = [k for k,x in enumerate(t) if x == i]
    cnt -= len(l)
    ans = max(cnt,ans)
print(ans)
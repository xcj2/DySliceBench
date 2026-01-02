import sys
import copy
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
INF = 1000000000000

a = LI()
k = I()

m = pow(3,k)
result = False
for i in range(m):
    val = copy.copy(a)
    for _ in range(k):
        tmp = i % 3
        i = i // 3
        val[tmp] = val[tmp]*2
    
    if(val[1] > val[0] and val[2] > val[1]):
        result = True

if(result):
    print('Yes')
else:
    print('No')
import sys
import math
sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,X,M = MI()


if M == 1:
    print(0)
    exit()

flag = [-1]*M
Z = [X]
flag[X] = 1
r = X
for i in range(2,M+2):
    r = r ** 2
    r %= M
    if flag[r] != -1:
        a,b = flag[r],i
        break
    else:
        flag[r] = i
        Z.append(r)

B = [0]*(len(Z))
for i in range(a-1):
    B[i] = 1
n = N-a+1
q = n//(b-a)
r = n % (b-a)

for i in range(a-1,a+r-1):
    B[i] = q+1
for i in range(a+r-1,b-1):
    B[i] = q

ans = 0
for i in range(len(Z)):
    ans += B[i]*Z[i]


print(ans)

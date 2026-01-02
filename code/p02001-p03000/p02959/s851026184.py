import sys,collections,math,random;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

n = I()
alis = Is()
blis = Is()
ans = 0
for i in range(n):
    if alis[i] >= blis[i]:
        ans += blis[i]
    elif alis[i] + alis[i+1] <= blis[i]:
        ans += alis[i] + alis[i+1]
        alis[i+1] = 0
    else:
        ans += blis[i]    
        alis[i+1] = max(0, alis[i] + alis[i+1] - blis[i])
print(ans)
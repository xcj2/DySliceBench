import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,p = map(int,readline().split())
lst1 = list(map(int,readline().split()))

def pow(n,p): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2
            p //= 2
        else:
            res = res * n
            p -= 1
    return res
#二項係数(modなし) O(k)
def large_conbination(n,k): #no mod. return nCk.
    res1 = 1
    for i in range(n,n-k,-1):
        res1*=i
    res2 = 1
    for i in range(1,k+1):
        res2*= i
    return res1//res2
od = 0
ev = 0
for i in lst1:
    if even(i):
        ev += 1
    else:
        od += 1

#奇数が偶数個
if even(p):
    ans = 0
    res = pow(2,ev)
    for i in range(0,od+1,2):
        ans += res*large_conbination(od,i)
#奇数が奇数個
else:
    ans = 0
    res = pow(2,ev)
    for i in range(1,od+1,2):
        ans += res*large_conbination(od,i)

print(ans)

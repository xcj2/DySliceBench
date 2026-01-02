Q = int(input())
mod = 10**6+3

fact_memo = [0]*mod
fact_memo[0] = 1
for n in range(mod-1):
    fact_memo[n+1] = (n+1)*fact_memo[n]%mod

def fact(n):
    if n>=mod:
        return 0
    else:
        return fact_memo[n]

def inv(n):
    n %= mod
    return pow(n,mod-2,mod)

def cal(x,d,n):
    if x == 0:
        print(0)
        return
    if d == 0:
        print(pow(x,n,mod))
        return
    ans = pow(d,n,mod)
    y = x*inv(d)%mod
    ans *= fact(y+n-1)
    ans %= mod
    ans *= inv(fact(y-1))
    ans %= mod
    print(ans)

for i in range(Q):
    cal(*map(int,input().split()))
import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

n = n_in()
x = s_in()

popcnt = sum(i == '1' for i in x)

def mod_add(a, b):
  return (a+b)%MOD

def mod_sub(a, b):
  return (a+MOD-b)%MOD

def mod_mul(a, b):
  return a*b%MOD

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = (1,0,a)
    w = (0,1,b)
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return (w[0],w[1])

def mod_inv(a):
    x,_  = extgcd(a, MOD)
    return (MOD+x%MOD)%MOD

def mod_div(a, b):
    return a*mod_inv(b)%MOD

def mod_pow(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

memo = {}

MOD = popcnt+1
memo[MOD] = []
for i in range(n):
    memo[MOD].append(mod_pow(2, i))
    

if popcnt-1 > 0:
    MOD = popcnt-1
    memo[MOD] = []
    for i in range(n):
        memo[MOD].append(mod_pow(2, i))

base_1 = 0
base_2 = 0
for i in range(n):
    if x[i] == '1':
        MOD = popcnt+1
        base_1 = mod_add(base_1, memo[MOD][n-i-1])

    
        if popcnt-1 > 0:
            MOD = popcnt-1
            base_2 = mod_add(base_2, memo[MOD][n-i-1])


for i in range(n):
    cnt = 0
    if x[i] == '0':        
        MOD = popcnt + 1
        current = mod_add(base_1, memo[MOD][n-i-1])
        cnt += 1
        while current > 0:
            MOD = sum(c=='1' for c in bin(current)[2:])
            current = current%MOD
            cnt += 1
    else:
        MOD = popcnt - 1
        if MOD == 0:
            print(0)
            continue
        current = mod_sub(base_2, memo[MOD][n-i-1])
        cnt += 1
        while current > 0:
            MOD = sum(c=='1' for c in bin(current)[2:])
            current = current%MOD
            cnt += 1

    print(cnt)

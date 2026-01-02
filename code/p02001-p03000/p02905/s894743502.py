# coding: utf-8
# Your code here!
def Eratosthenes(N): #N以下の素数のリストを返す
    N+=1
    is_prime_list = [True]*N
    m = int(N**0.5)+1
    for i in range(3,m,2):
        if is_prime_list[i]:
            is_prime_list[i*i::2*i]=[False]*((N-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,N,2) if is_prime_list[i]]

#aを破壊的にgcd-zetaする
def zeta_gcd(a,primes):
    n = len(a)-1
    for p in primes:
        for i in range(n//p,0,-1):
            a[i] += a[p*i]
            a[i] %= MOD
#    return a

#aを破壊的にgcd-mobiusする
def mobius_gcd(a,primes):
    n = len(a)
    for p in primes:
        for i in range(1,n):
            if i*p >= n: break
            a[i] -= a[p*i] 
            a[i] %= MOD
#    return a

################################################

#################################################

SIZE=1000001; MOD=998244353 #ここを変更する

SIZE += 1
inv = [0]*SIZE  # inv[j] = j^{-1} mod MOD
inv[1] = 1
for i in range(2,SIZE):
    inv[i] = MOD - (MOD//i)*inv[MOD%i]%MOD

################################################
#################################################
import sys
#sys.setrecursionlimit(10**6)
readline = sys.stdin.readline 

n = int(input())
a = [int(i) for i in readline().split()]

num = [0]*SIZE
for i in a: num[i] += i

primes = Eratosthenes(SIZE)

zeta_gcd(num,primes)
ans = [i*i for i in num]
mobius_gcd(ans,primes)

res = 0
for i,c in enumerate(ans):
    res = (res + c*inv[i])%MOD
for i in a:
    res = (res-i)%MOD
        
print(res*inv[2]%MOD)








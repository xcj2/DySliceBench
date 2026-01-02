import math
mod = 10**9+7

# 素因数分解、辞書で返すやつ
# mathをimportする
def prime(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
        if num > n:
            break
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor

#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m=mod):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

dic = {}
for a in A:
    pr = prime(a)
    for num, count in pr.items():
        if not num in dic.keys():
            dic[num] = count
        else:
            if dic[num] < count:
                dic[num] = count

lcm = 1
for num, count in dic.items():
    lcm *= pow(num, count, mod)
    lcm %= mod

ans = 0
for a in A:
    ans += mod_inv(a)*lcm
    ans %= mod

print(ans)

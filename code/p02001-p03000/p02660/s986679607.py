def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from math import sqrt

N = INT()
tmp = N
fact = {}

for n in range(2, int(sqrt(N)) + 1):
    if tmp == 1:
        break
    
    e = 0
    while 1:
        if tmp % n != 0:
            break
        tmp //= n
        e += 1
    
    if e == 0:
        continue

    fact[n] = e

if tmp != 1:
    fact[tmp] = 1

if fact == {}:
    fact[N] = 1

ans = 0

for p in fact.keys():
    e = 1
    z = p
    
    if N == 1:
        break
    
    while 1:
        if N % z != 0:
            break
        N //= z
        e += 1
        z = pow(p, e)
        ans += 1
        
print(ans)
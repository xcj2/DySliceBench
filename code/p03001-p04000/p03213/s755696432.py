import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import Counter

def factorize(n: int):
    d = Counter()
    m= 2
    
    while m*m <= n:
        while n%m == 0:
            n //= m
            d[m] += 1
            
        m += 1
        
    if n > 1:
        d[n] += 1
        
    return d


# 各階乗での素因数リストを出す。
n = ni()
divs = Counter()
for i in range(2,n+1):
    divs += factorize(i)
    


ans = 0
# 4,4,2以上を満たすペアを探す
gteq4 = []
lt4gteq2 = []
for k,v in divs.items():
    if v >= 4:
        gteq4.append(k)
    elif 2 <= v < 4:
        lt4gteq2.append(k)
        

# 4,4,4以上のみ
len_gteq4 = len(gteq4)
if len_gteq4 >= 3:
    ans += (len_gteq4*(len_gteq4-1)*(len_gteq4-2) // 6) * 3

# 4,4,2or3のみ
len_lt4gteq2 = len(lt4gteq2)
if len_gteq4 >= 2 and len_lt4gteq2 >= 1:
    ans += (len_gteq4*(len_gteq4-1)//2) * len_lt4gteq2
    
    
# 2,24以上を満たすペアを探す
gteq24 = []
gteq2 = []
for k,v in divs.items():
    if v >= 24:
        gteq24.append(k)
    if v >= 2:
        gteq2.append(k)
        
ans += (len(gteq24) * len(gteq2) - len(gteq24))


# 4,14以上を満たすペアを探す
gteq14 = []
for k,v in divs.items():
    if v >= 14:
        gteq14.append(k)

ans += (len(gteq14) * len(gteq4) - len(gteq14))


# 74以上のものを探す
gteq74 = []
for k,v in divs.items():
    if v >= 74:
        gteq74.append(k)
        
ans += len(gteq74)
        
print(ans)
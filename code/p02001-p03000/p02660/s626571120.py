import sys
sys.setrecursionlimit(1000000)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
from collections import defaultdict
n = I()
def primes(n):
    cnt = defaultdict(int)
    for i in range(2,int(n**0.5)+1): # range(3)だと、0,1,2が出てくる。
        while n % i == 0:
            cnt[i] += 1 # 同じ素数で何回割れるか辞書型で登録しておく
            n //= i # iで割り切った商で更新しておく
    if n > 1: # nの平方根より大きい値があった場合、追加
        cnt[n] += 1
    return cnt
prs = primes(n) #　素数の辞書
ans = 0
for key in prs.keys(): #辞書から素数を抽出して、その素数の指数値をvとして格納する。
    v = prs[key]
    for i in range(100):
        # if (i * (i+1)) // 2 <= v:　これだと何度も足し算してしまう。
        if (i * (i + 1)) // 2 > v: # 指数eを超えた一つ前が目的の計数である。
            ans += (i-1)
            break
print(ans)

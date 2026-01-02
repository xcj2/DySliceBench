n=int(input())
import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright
from fractions import Fraction as frac  #frac(a,b)で正確なa/b
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########


def Dlist(BIG):
    D=[1]*(BIG+1)
    for p in range(2,BIG+1):
        if D[p]!=1:
            continue
        for i in range(p,BIG+1,p):
            if D[i]==1:
                D[i]=p
    return D
# Dlist(10) -> [1, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2]

def BUNKAI(num,D):
    now=num ; ans=[]
    while now>1:
        ans.append(D[now])
        now//= D[now]
    # return ans
    return Counter(ans)
# print(BUNKAI(3012,Dlist(3012))) -> Counter({2: 2, 3: 1, 251: 1})

def SOINSU(num,D): #素因数だけ列挙(setしただけ)
    now=num ; ans=set()
    while now>1:
        ans.add(D[now])
        now//=D[now]
    return ans
# print(SOINSU(3012,Dlist(3012)))　-> {2, 3, 251}
D=Dlist(n)
ans=0
for i  in range(1,n):
    now=1
    l=BUNKAI(i,D)
    for j in l.values():
        now*=j+1
    ans+=now
print(ans)
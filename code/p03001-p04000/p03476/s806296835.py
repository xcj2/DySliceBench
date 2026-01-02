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

from math import sqrt
from bisect import bisect_left, bisect_right

# 半開区間[lower, upper)の素数のリストを作成する
def make_prime_list(lower:int, upper:int) -> list:
    
    # 素数リストの初期化    
    isPrime = [True]*upper
    primeList = []
    
    # 区間内の数字が0,1のみならここで終了
    if upper <= 2:
        return primeList
    
    # 区間内の数字に2以上のものがあるとき
    isPrime[0] = False
    isPrime[1] = False
    
    # エラトステネスの篩の処理
    for n in range(2,int(sqrt(upper))+2):
        if isPrime[n]:
            res=2*n
            while res<upper:
                isPrime[res] = False
                res += n
    
    # 区間内の素数を抽出
    for n in range(lower,upper):
        if isPrime[n]:
            primeList.append(n)
        
    return primeList

q = ni()
query = [tuple(li()) for _ in range(q)]

prime_list = set(make_prime_list(2,10**5+1))

like2017 = []

for i in range(3, 10**5, 2):
    if (i in prime_list) and ((i+1)//2 in prime_list):
        like2017.append(i)
        
for l,r in query:
    print(bisect_right(like2017, r) - bisect_left(like2017, l))
    

from math import sqrt
from collections import defaultdict 

# 半開区間[lower, upper)の素数のリストを作成する
def make_prime_list(lower:int, upper:int) -> list:
    
    # 変数のバリデーション
    if lower < 0:
        raise ValueError("lowerは0以上でなければいけません。(lower:{})".format(lower))

    elif upper <= lower:
        raise ValueError("upperはlowerより大きい数でなければいけません。\
                         (lower:{}, upper:{})".format(lower,upper))
    
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


# numを素因数分解する
def factoring(num: int, prime_list:list) -> dict:
    
    # バリデーション
    if num < 2:
        raise ValueError("numは2以上でなければいけません。(num:{})".format(num))
    
    
    # numまでの素数リストを作る
    prime_set = set(prime_list)
    
    # {素数: 含まれる数}の辞書を作る
    dic = defaultdict(int)
    res = num
    i = 0
    
    # resが素数になるまでdicに素因数を詰め続ける
    while not res in prime_set:
        if res % prime_list[i] == 0:
            dic[prime_list[i]] += 1
            res //= prime_list[i]
        
        else:
            i += 1
            if i >= len(prime_list):
                break
            
    dic[res] += 1
    
    return dic

# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())


MOD = 10**9 + 7
n = ni()

# nまでの素数リストを作る
prime_list = make_prime_list(0,n+1)

# 素因数の辞書
dic = defaultdict(int)
for num in range(2,n+1):
    fac = factoring(num, prime_list)
    for k,v in fac.items():
        dic[k] += v

# 約数は各素因数の数を+1して掛け算したもの
ans = 1
for v in dic.values():
    ans = ans*(v+1) % MOD
    
print(ans)
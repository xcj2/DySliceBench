import math
import bisect
import collections
import itertools
def gcd(a,b):return math.gcd #最大公約数
def lcm(a,b):return (a*b) // math.gcd(a,b) #最小公倍数
def iin(): return int(input()) #整数読み込み
def imn(): return map(int, input().split()) #整数map取得
def iln(): return list(map(int, input().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

X = iin()

while True:
    if is_prime(X):
        print(X)
        break
    X += 1


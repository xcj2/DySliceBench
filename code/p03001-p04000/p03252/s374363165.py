import sys
from collections import Counter
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]  # LIST INT
def LF(): return [float(x) for x in sys.stdin.readline().split()]  # LIST FLOAT
def LS(): return sys.stdin.readline().split()  # LIST STRING
def MI(): return map(int, sys.stdin.readline().split())  # MAP INT
def II(): return int(sys.stdin.readline())  # INPUT INT
def IS(): return input()  # INPUT STRING
def P(x): return print(x)
def C(x): return Counter(x)


S = C(IS())
T = C(IS())
sv = sorted([v for v in S.values()])
tv = sorted([v for v in T.values()])
P('Yes') if sv == tv else P('No')  # これはうそ S = 'zazel' T = 'apple'でダメ

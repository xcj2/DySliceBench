import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

N = I()
X = LI()

#  N = 200000
#  X = [i*10 for i in range(1,N+1)]

"""
まずは偶数時の中央値のidxを求める
偶数時の中央値より小さいものが抜かれたときは、そのまま、
大きいものが抜かれたときはidx-1が中央値となる
"""
#見つかったメディアンを保存
found = {}
sorted_X = sorted(X)
median = sorted_X[int(len(X)/2)]
for x in X:
    #  print('x', x)
    #  print('found', found)
    if x < median:
        if found.get('small',None):
            print(found['small'])
        else:
            print(median)
            found['small'] = median
    elif x > median:
        if not found.get('big', None):
            tmp = [i for i in sorted_X]
            tmp.remove(x)
            #奇数長になっている
            m = tmp[int(len(tmp)//2)]
            print(m)
            found['big'] = m
        else:
            print(found['big'])
    else:
        if not found.get('equal', None):
            tmp = [i for i in sorted_X]
            tmp.remove(x)
            m = tmp[int(len(tmp)//2)]
            print(m)
            found['equal'] = m
        else:
            print(found['equal'])

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
def S(): return input()
def pf(s): return print(s, flush=True)

D, G = LI()
PC = []
for i in range(D):
    PC.append([(i+1)*100] + LI())

PC = [tuple(i) for i in PC]

# 全探索でよくね
# 組み合わせを選んで、高いほうから選んでいく。
# 組み合わせの数が少ない順に試していく
"""
1種類の場合
2種類の場合
3種類の場合
...
10種類の場合
Gを超えだしたらその種類数の中で決める。

10Cr
という形になる。
最大でも組み合わせの数は260通りほどなのでいけそうだ。
"""
results = []
def dfs(ls, limit, combis, count):
    is_end = True
    for i in range(len(ls)):
        #  print('saiki i, ls', i, ls)
        new_list = [_ for _ in ls]
        if new_list[i] < combis[i][1]:
            # 余力があればプラス
            new_list[i] += 1
            is_end = False

            p = 0
            for idx, j in enumerate(ls):
                #  if ls == [2,5]:
                #      import pdb
                #      pdb.set_trace()
                # 点数計算
                p += combis[idx][0] * j
                if j == combis[idx][1]:
                    p += combis[idx][2]

            if p >= G:
                results.append(count)
                return

            dfs(new_list, limit, combis, count+1)

# 完答しない場合もある。
result = 0
count = 0
for i in range(PC[-1][1]):
    result += PC[-1][0]
    count += 1
    if result >= G:
        results.append(count)
for i in range(1, D+1):
    # i種類の組み合わせを選ぶ
    combis = list(itertools.combinations(PC, i))
    #  print('i, combis', i, combis)
    for combi in combis:
        limit = sum([j[1] for j in PC])
        # iは完答する種類数
        result = 0
        result += sum([c[0] * c[1] + c[2] for c in combi])
        count = sum([c[1] for c in combi])
        if result >= G:
            results.append(count)
            continue
        rest = [_ for _ in PC if _ not in combi]
        for r in rest[::-1]:
            for ridx in range(r[1]):
                result += r[0]
                count += 1
                if result >= G:
                    results.append(count)

                

print(min(results))


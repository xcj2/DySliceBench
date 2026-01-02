"""
                            pppppppppppppppppppp
                         ppppp  ppppppppppppppppppp
                      ppppppp    ppppppppppppppppppppp
                      pppppppp  pppppppppppppppppppppp
                      pppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppppp
       ppppppppppppppppppppppppppppppppppppppppppppppp  pppppppppppppppppppp
      pppppppppppppppppppppppppppppppppppppppppppppppp  ppppppppppppppppppppp
     ppppppppppppppppppppppppppppppppppppppppppppppppp  pppppppppppppppppppppp
    ppppppppppppppppppppppppppppppppppppppppppppppp    pppppppppppppppppppppppp
   pppppppppppppppppppppppppppppppppppppppppppppp     pppppppppppppppppppppppppp
  ppppppppppppppppppppppppppppppppppppppppppppp      pppppppppppppppppppppppppppp
  pppppppppppppppppppppppppppppppp               pppppppppppppppppppppppppppppppp
  pppppppppppppppppppppppppppp     pppppppppppppppppppppppppppppppppppppppppppppp
  ppppppppppppppppppppppppppp    pppppppppppppppppppppppppppppppppppppppppppppppp
    pppppppppppppppppppppppp  pppppppppppppppppppppppppppppppppppppppppppppppppp
     ppppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppppppp
      pppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppppp
       ppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppppp
                              pppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppp  pppppppp
                              ppppppppppppppppppppp    ppppppp
                                 ppppppppppppppppppp  ppppp
                                    pppppppppppppppppppp
"""


import sys
from functools import lru_cache, cmp_to_key
from collections import defaultdict as dd, deque, Counter as C
from bisect import bisect_left as bl, bisect_right as br, bisect
from heapq import heapify, heappop, heappush
# from math import sqrt
from math import ceil, log, floor
mod = pow(10, 9) + 7
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(var, end="\n"): sys.stdout.write(str(var)+end)
def outa(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]

# Code is referenced from https://geeksforgeeks.org

#
# segment = [[] for i in range(1000)]
#
#
# def build(i, s, e, arr):
#     if s == e:
#         segment[i].append(arr[s])
#         return
#     build(2 * i, s, (s + e) // 2, arr)
#     build(1 + 2 * i, 1 + (s + e) // 2, e, arr)
#     segment[i].append(segment[2 * i])
#     segment[i].append(segment[2 * i + 1])
#
#
# def query(node, l, r, a, b):
#     left, right, result = [], [], []
#     if b < l or a > r:
#         return result
#     if a <= l and r <= b:
#         return segment[node]
#     left = query(2 * node, l, (l + r) // 2, a, b)
#     result.append(left)
#     right = query(1 + 2 * node, 1 + (l + r) // 2, r, a, b)
#     result.append(right)
#     return result
#
#
# def answer(ans):
#     d = {}
#     for i in str(ans):
#         if i not in ['[', ',', ']', ' ']:
#             d[i] = 1
#     return len(d)
#
#
# def init(n):
#     h = ceil(log(n, 2))
#     h = (2 * (pow(2, h))) - 1
#
#
# def getDistinct(l, r, n):
#     ans = query(1, 0, n - 1, l, r)
#     print(answer(str(ans)))
#
#
# n, q = sp()
# arr = L()
# init(n)
# build(1, 0, n - 1, arr)
# for _ in range(q):
#     l, r = sp()
#     getDistinct(l-1, r-1, n)


MAX = 1000001


class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx


def update(idx, val, bit, n):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx


def query(idx, bit, n):
    summ = 0
    while idx:
        summ += bit[idx]
        idx -= idx & -idx
    return summ


def answeringQueries(arr, n, queries, q):
    bit = [0] * (n + 1)
    last_visit = [-1] * MAX
    ans = [0] * q

    query_counter = 0
    for i in range(n):
        if last_visit[arr[i]] != -1:
            update(last_visit[arr[i]] + 1, -1, bit, n)
        last_visit[arr[i]] = i
        update(i + 1, 1, bit, n)
        while query_counter < q and queries[query_counter].r == i:
            ans[queries[query_counter].idx] = query(queries[query_counter].r + 1, bit, n) - query(queries[query_counter].l, bit, n)
            query_counter += 1
    for i in range(q):
        print(ans[i])


if __name__ == "__main__":
    n, q = sp()
    a = L()
    queries = []
    for i in range(q):
        l, r = sp()
        queries.append(Query(l-1, r-1, i))
    queries.sort(key=lambda x: x.r)
    answeringQueries(a, n, queries, q)

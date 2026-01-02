def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from sys import exit

import sys
sys.setrecursionlimit(1000000000)
mod = 998244353

#############
# Main Code #
#############

N, X, M = getNM()
# 一つしかないなら二度と出ない
lista = [[-1, -1] for i in range(M)]

n = X
for i in range(2 * M + 1):
    if lista[n][0] == -1:
        lista[n][0] = i
    elif lista[n][1] == -1:
        lista[n][1] = i
    n *= n
    n %= M

cnt = 0
for i in range(M):
    s, e = lista[i]
    # ループする
    if s >= 0 and e >= 0:
        cnt += i * (((N - 1) - s) // (e - s) + 1)
    # 1回きり
    elif s >= 0:
        cnt += i
print(cnt)
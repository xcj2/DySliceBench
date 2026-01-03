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

from collections import defaultdict, deque, Counter

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

H, W, N = map(int, input().split())
query = [list(map(int, input().split())) for i in range(N)]
list_star = defaultdict(set)
H_max = 0
W_max = 0
for y, x in query:
    H_max = max(H_max, y)
    W_max = max(W_max, x)
    list_star[y - 1].add(x - 1)

dx = [0, 0, 1, 1, 1, 0, -1, -1, -1]
dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]


lista = [0] * 10

def counter(x, y):
    if x <= 0 or W - 1 <= x or y <= 0 or H - 1 <= y:
        return 0
    cnt = 0
    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H:
            if nx in list_star[ny]:
                cnt += 1
    return cnt

star_list = set()
for y, x in query:
    x -= 1
    y -= 1
    for l in range(9):
        nx = x + dx[l]
        ny = y + dy[l]
        star_list.add((nx, ny))

star_list = list(star_list)
for x, y in star_list:
    if not (x <= 0 or W - 1 <= x or y <= 0 or H - 1 <= y):
        lista[counter(x, y)] += 1

left = (H - 2) * (W - 2) - sum(lista)
lista[0] = left
for i in lista:
    print(i)
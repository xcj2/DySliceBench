import sys
import heapq
from collections import defaultdict

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, K = na()

A_array = na()

cusum = 0
mod_array = [0]
for i, a in enumerate(A_array):
    cusum = (cusum + a) % K
    mod = (cusum + K - (i+1)) % K
    mod_array.append(mod)

# print(mod_array)

ans = 0
mod_queue = []
cnt_dic = defaultdict(int)
for i, v in enumerate(mod_array):
    heapq.heappush(mod_queue, (i, 1, v))

while(len(mod_queue)):
    i, q, v = heapq.heappop(mod_queue)
    if q == 1:
        ans += cnt_dic[v]
        cnt_dic[v] += 1
        if i + K <= N:
            heapq.heappush(mod_queue, (i+K-0.5, 2, v))
    else:
        cnt_dic[v] -= 1
    # print(i, v, q, ans)

print(ans)

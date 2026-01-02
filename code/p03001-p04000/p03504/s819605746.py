import sys
import numpy as np
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


N, C = mi()
time = [0 for i in range(10 ** 5 + 10)]
use = [[] for i in range(10 ** 5 + 10)]
F = []
for i in range(N):
    F.append(lmi())
F.sort(key=lambda x: x[0])
# print(F)
for s, t, c in F:
    use[t].append(c)
    if c in use[s]:
        time[s] += 1
    else:
        time[s-1] += 1
    time[t] -= 1
# print(time[0:100])
timesum = np.cumsum(np.array(time))
# print(use[0:100])
print(max(timesum))
import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return list(map(int, sys.stdin.readline().split()))
def II(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
from collections import defaultdict

n = II()
tasks = [0 for i in range(n)]
for i in range(n):
    tasks[i] = LI()
tasks = sorted(tasks, key=lambda x: x[1])
load = 0
for i in range(n):
    load += tasks[i][0]
    if load > tasks[i][1]:
        print("No")
        break
else:
    print("Yes")
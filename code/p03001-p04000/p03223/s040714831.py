import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import deque

n = ni()
a = [ni() for _ in range(n)]

a.sort()

b = a.copy()
c = a.copy()

# 小さい順に詰める
bdeq = deque(b)
bret = deque()

bret.append(bdeq.popleft())
push_small = False
while len(bdeq) > 1:
    if push_small:
        bret.append(bdeq.popleft())
        bret.appendleft(bdeq.popleft())
        push_small = False

    else:
        bret.append(bdeq.pop())
        bret.appendleft(bdeq.pop())
        push_small = True

if len(bdeq) > 0:
    if abs(bdeq[0] - bret[0]) > abs(bdeq[0] - bret[-1]):
        bret.appendleft(bdeq[0])
    else:
        bret.append(bdeq[0])

# 大きい順に詰める
cdeq = deque(c)
cret = deque()

cret.append(cdeq.pop())
push_small = True
while len(cdeq) > 1:
    if push_small:
        cret.append(cdeq.popleft())
        cret.appendleft(cdeq.popleft())
        push_small = False

    else:
        cret.append(cdeq.pop())
        cret.appendleft(cdeq.pop())
        push_small = True

if len(cdeq) > 0:
    if abs(cdeq[0] - cret[0]) > abs(cdeq[0] - cret[-1]):
        cret.appendleft(cdeq[0])
    else:
        cret.append(cdeq[0])

# 答えが大きいほうを選択
bans = 0
for i in range(n-1):
    bans += abs(bret[i] - bret[i+1])

cans = 0
for i in range(n-1):
    cans += abs(cret[i] - cret[i+1])

print(max(bans, cans))

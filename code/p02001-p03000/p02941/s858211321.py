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


from heapq import heappush, heappop

n = ni()
a = list(li())
b = list(li())

# n = 10**5
# a = [1]*(10**5)
# b = [5] + [1]*(10**5-2) + [7]

que = []

for i, bi in enumerate(b):
    heappush(que, (-bi, i))

ans = 0
while que:

    cur, position = heappop(que)
    cur = -cur

    if cur - b[(position-1)%n] - b[(position+1)%n] < a[position]:
        continue

    ope = (cur - a[position]) // (b[(position-1)%n] + b[(position+1)%n])

    ans += ope
    b[position] -= ope * (b[(position-1)%n] + b[(position+1)%n])
    heappush(que, (-b[position], position))

ok = True
for ai, bi in zip(a, b):
    if ai != bi:
        ok = False

if ok:
    print(ans)
else:
    print(-1)
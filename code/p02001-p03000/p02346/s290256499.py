import sys

def initialize(N):
    i = 1
    while i < N:
        i *= 2
    return [0] * (2 * i - 1), i

def add(i, x, L, d):
    K = i + d - 1
    L[K] += x
    while K > 0:
        K = (K-1)//2
        L[K] += x

def getSum(s, t, index, l, r, L): 
    if r <= s or t <= l: return 0
    elif s <= l and r <= t: return L[index]
    else:
        sumL = getSum(s, t, 2 * index + 1, l, (l+r)//2, L)
        sumR = getSum(s, t, 2 * index + 2, (l+r)//2, r, L)
        return sumL + sumR

F = sys.stdin
N, Q = map(int, F.readline().strip("\n").split(" "))
SegTree, d = initialize(N)
for _ in range(Q):
    com, x, y = map(int, F.readline().strip("\n").split(" "))
    if com == 0: add(x-1, y, SegTree, d)
    elif com == 1:
        print(getSum(x-1, y, 0, 0, d, SegTree))

from sys import exit, setrecursionlimit
import sys
from io import StringIO

def read():
    return int(input())

def reads():
    return [int(x) for x in input().split()]

setrecursionlimit(1000000)

# inputstr = """
# 2 10 4
# 20
# 20
# """[1:]
# sys.stdin = StringIO(inputstr)

(N, A, B) = reads()
H = [0] * N

for i in range(N):
    H[i] = read()

def satisfy(t):
    q = A - B
    cnt = sum((max(h-B*t, 0) + q - 1)//q for h in H)
    return cnt <= t

(l, r) = (0, 10**9)

while True:
    if l + 1 == r:
        break
    m = (l + r) // 2
    if satisfy(m):
        r = m
    else:
        l = m

print(r)
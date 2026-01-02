from collections import deque


def nextj(n):
    while S[n] == '0':
        n += 1
        if n == N:
            return N
    q.appendleft(n)
    while S[n] == '1':
        n += 1
        if n == N:
            return N
    return n


def init(n):
    while S[n] == '1':
        n += 1
        if n == N:
            return N
    return n


def calc():
    q.appendleft(0)
    ans = 0
    j = init(0)
    if j == N:
        return N
    for _ in range(K - 1):
        j = nextj(j)
        if j == N:
            return N
    while True:
        j = nextj(j)
        ans = max(ans, j - q.pop())
        if j == N:
            return ans


N, K = map(int, input().split())
S = input()
q = deque()
print(calc())

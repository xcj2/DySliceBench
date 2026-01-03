# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

from collections import deque

def logical_and(x, y):
    z = deque([])

    for i in range(len(x)):
        a = x.popleft()
        for j in range(len(y)):
            b = y[j]
            if a == b:
                del y[j]
                z.append(a)
                break
    # print(z)
    return z

def solve():
    n = II()
    S = [deque(sorted(list(input()))) for _ in range(n)]

    c = S[0]
    for i in range(1, n):
        s = S[i]
        c = logical_and(c, s)

    c = sorted(c)
    print(''.join(c))


if __name__ == '__main__':
    solve()

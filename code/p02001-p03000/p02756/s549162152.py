import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')

from collections import deque
def solve():
    S = deque(list(input()))

    Q = II()
    rev = False
    for i in range(Q):
        q = list(input().split())
        # print(q)
        if q[0] == '1':
            rev = ~rev
        else:
            op = q[1]
            if (op == '1' and not rev) or op == '2' and rev:
                S.appendleft(q[2])
            else:
                S.append(q[2])

    S = list(S)
    if rev:
        S = S[::-1]

    print(''.join(S))

if __name__ == '__main__':
    solve()

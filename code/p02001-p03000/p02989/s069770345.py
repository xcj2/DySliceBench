import sys
sys.setrecursionlimit(10 ** 9)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

from collections import deque

def solve():
    n = II()
    D = deque(sorted(LI()))

    for i in range(n):
        l = D.popleft()
        # print('l', l)
        if len(D) == 0:
            print(1)
            break
        else:
            r = D.pop()
            # print('r', r)
            if len(D) == 0:
                print(r - l)
                break
            else:
                continue




if __name__ == '__main__':
    solve()

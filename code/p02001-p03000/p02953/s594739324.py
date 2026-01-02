# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

from collections import deque

def solve():
    n = II()
    H = LI()
    d = deque([])

    flag = True
    for i in range(0, n):
        hi = H[i]
        if i == 0:
            d.append(hi - 1)
            continue

        hp = d.popleft()
        if hp < hi:
            d.append(hi - 1)
        elif hp == hi:
            d.append(hi)
        else:   # hp > hi
            flag = False
            break

    print('Yes' if flag else 'No')







if __name__ == '__main__':
    solve()

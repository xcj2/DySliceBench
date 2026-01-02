# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    n = II()
    H = LI()

    pre = -999
    flag = True
    for h in H:
        if pre <= h - 1:
            pre = h - 1
        elif pre <= h:
            pre = h
        else:
            flag = False
            break

    print('Yes' if flag else 'No')

if __name__ == '__main__':
    solve()

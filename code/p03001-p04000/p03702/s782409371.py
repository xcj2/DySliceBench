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


def judge(k: int, h: list, a:int, b:int):
    h = [max(0, hi - k*b) for hi in h]
    cnt = 0
    for hi in h:
        cnt += -(-hi//(a-b))

    return True if cnt <= k else False

def binary_search(h, a, b):
    low = 0
    high = 10**18

    while high - low > 1:
        mid = (high+low) // 2
        if judge(mid, h, a, b):
            high = mid
        else:
            low = mid

    return high

n, a, b = li()
h = [ni() for _ in range(n)]

print(binary_search(h, a, b))

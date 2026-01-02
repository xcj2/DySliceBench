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

def solve():
    n, m = MI()
    A = LI()

    s = sum(A)
    cnt = 0
    for a in A:
        if a * 4 * m >= s:
            cnt += 1
    print('Yes' if cnt >= m else 'No')


if __name__ == '__main__':
    solve()

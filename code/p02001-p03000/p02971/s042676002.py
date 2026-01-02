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
    A = [II() for _ in range(n)]
    A2 = sorted(A, reverse=True)
    mx = A2[0]
    mx2 = A2[1]

    for a in A:
        if a == mx:
            print(mx2)
        else:
            print(mx)


if __name__ == '__main__':
    solve()

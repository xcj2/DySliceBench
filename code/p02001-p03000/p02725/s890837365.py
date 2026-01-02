# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    k, n = MI()
    A = LI()

    path = [A[i] - A[int1(i)] for i in range(1, len(A))]
    l = A[-1] - A[0]
    path.append(min(l, k - l))
    # print(path)

    ans = sum(path)
    if len(path) > 2:
        ans = ans - max(path)
    print(ans)


if __name__ == '__main__':
    solve()

# import sys
# sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def solve():
    n, x, y = MI()

    def dist(a, b):
        return b - a

    ans = [0 for _ in range(n-1)]
    for i in range(1, n):
        for j in range(i+1, n+1):
            if i <= x and y <= j:
                d = dist(i, x) + 1 + dist(y, j)
            elif x < i < y:
                if x < j < y:
                    d = min(dist(i, j), dist(x, i) + 1 + dist(j, y))
                else:
                    d = min(dist(x, i)+1, dist(i, y)) + dist(y, j)
            elif x < j < y:
                d = min(dist(i, j), dist(i, x) + 1 + dist(j, y))
            else:
                d = dist(i, j)
            # print(i, j, d)
            ans[d-1] += 1
    print("\n".join(map(str, ans)))



if __name__ == '__main__':
    solve()

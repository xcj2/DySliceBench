import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(m)]

    def is_ok(L):
        for s, c in query:
            if L[s - 1] != c:
                break
        else:
            print("".join(map(str, L)))
            exit()
        return

    def dfs(X):
        if len(X) == n:
            x = int("".join(map(str, X)))
            if len(str(x)) == n:
                is_ok(X)
            return

        for i in range(10):
            X.append(i)
            dfs(X)
            X.pop()

    dfs([])
    print(-1)


if __name__ == '__main__':
    resolve()

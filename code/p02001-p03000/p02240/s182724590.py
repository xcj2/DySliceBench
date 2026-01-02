import sys
readline = sys.stdin.readline
def MAIN():
    n, m = map(int, input().split())
    li = [i for i in range(n)]
    def f(a):
        if li[a] == a:
            return a
        li[a] = f(li[a])
        return li[a]
    def f2(a, b):
        if li[a] == a:
            li[a] = b
            return
        f2(li[a], b)
        li[a] = b
    for _ in range(m):
        x, y = map(int, readline().split())
        if f(x) > f(y):
            f2(x, li[y])
        elif f(x) < f(y):
            f2(y, li[x])
    for _ in range(int(input())):
        x, y = map(int, readline().split())
        print("yes" if f(x) == f(y) else "no")
MAIN()


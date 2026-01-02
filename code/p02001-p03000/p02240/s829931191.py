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
        else:
            f2(li[a], b)
            li[a] = b
    def solve(a, b):
        if f(a) == f(b):
            return "yes"
        return "no"
    for _ in range(m):
        x, y = map(int, readline().split())
        if f(x) > f(y):
            f2(x, li[y])
        else:
            f2(y, li[x])
    for _ in range(int(input())):
        x, y = map(int, readline().split())
        print(solve(x, y))
MAIN()

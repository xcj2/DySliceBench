import sys
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N, M = mi()
    l = [[] for i in range(N)]
    for i in range(M):
        a, b = mi()
        l[a-1].append(b-1)
        l[b-1].append(a-1)

    for v in l[0]:
        if N-1 in l[v]:
            print('POSSIBLE')
            return
    print('IMPOSSIBLE')


if __name__ == '__main__':
    main()

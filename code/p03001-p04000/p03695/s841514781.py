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
    N = ii()
    a = list(mi())
    d = [0]*9
    for i in range(N):
        if a[i] < 400:
            d[0] = 1
        elif a[i] < 800:
            d[1] = 1
        elif a[i] < 1200:
            d[2] = 1
        elif a[i] < 1600:
            d[3] = 1
        elif a[i] < 2000:
            d[4] = 1
        elif a[i] < 2400:
            d[5] = 1
        elif a[i] < 2800:
            d[6] = 1
        elif a[i] < 3200:
            d[7] = 1
        else:
            d[8] += 1

    print(max(1, sum(d[:-1])), sum(d))


if __name__ == '__main__':
    main()

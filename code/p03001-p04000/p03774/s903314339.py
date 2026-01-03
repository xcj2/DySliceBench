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
    a, b = i2(N)
    c, d = i2(M)

    for i in range(N):
        dist = 10**10
        for j in range(M):
            if dist > abs(a[i]-c[j])+abs(b[i]-d[j]):
                cp = j+1
                dist = abs(a[i]-c[j])+abs(b[i]-d[j])
        print(cp)

if __name__ == '__main__':
    main()

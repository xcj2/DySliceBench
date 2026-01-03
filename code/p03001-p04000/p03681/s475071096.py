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
    fact = [1]
    for i in range(1, max(N, M)+3):
        fact.append((i*fact[-1])%MOD)
    if abs(N-M) == 1:
        print((fact[N]*fact[M])%MOD)
    elif N == M:
        print((2*fact[N]*fact[M])%MOD)
    else:
        print(0)



if __name__ == '__main__':
    main()

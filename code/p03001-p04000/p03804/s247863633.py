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
    A = [input() for i in range(N)]
    B = [input() for i in range(M)]

    for x in range(N-M+1):
        for y in range(N-M+1):
            bl = True
            for i in range(M):
                for j in range(M):
                    if A[x+i][y+j] != B[i][j]:
                        bl = False
            if bl:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()

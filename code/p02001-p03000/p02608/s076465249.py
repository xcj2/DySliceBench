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
    l = [0]*(N+1)
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                t = x*x+y*y+z*z+x*y+y*z+z*x
                if t <= N:
                    l[t] += 1
    print(*l[1:], sep='\n')

if __name__ == '__main__':
    main()

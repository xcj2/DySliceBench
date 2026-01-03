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
    s = [ii() for i in range(N)]
    s.sort()
    ans = sum(s)
    if ans%10:
        print(ans)
        return
    for i in range(N):
        if (ans-s[i])%10!=0:
            print(ans-s[i])
            return
    print(0)

if __name__ == '__main__':
    main()

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
    even = sum(1 for i in range(N) if a[i]%2==0)
    odd = sum(1 for i in range(N) if a[i]%2==1)
    four = sum(1 for i in range(N) if a[i]%4==0)

    if odd-four == 1:
        ans = (odd+four == N)
    elif odd <= four:
        ans = True
    else:
        ans = False

    print('Yes' if ans else 'No')
    


if __name__ == '__main__':
    main()

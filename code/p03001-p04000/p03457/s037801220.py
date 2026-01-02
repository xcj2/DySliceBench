import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())


def main():
    N = ii()
    txy = [list(mi()) for i in range(N)]
    t, x, y = [list(i) for i in zip(*txy)]
    if t[0]-x[0]-y[0] < 0 or (t[0]-x[0]-y[0])%2:
        print('No')
        return
    for i in range(N-1):
        k = t[i+1]-t[i]-abs(x[i+1]-x[i])-abs(y[i+1]-y[i])
        if k < 0 or k%2:
            print('No')
            return
    print('Yes')
    


if __name__ == '__main__':
    main()

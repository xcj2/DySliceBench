import sys
sys.setrecursionlimit(500000)

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
    H, W, K = mi()
    c = [list(input()) for i in range(H)]
    cnt = 0

    for row in range(2**H):
        for column in range(2**W):
            tmp = [['.']*W for i in range(H)]
            for i in range(H):
                for j in range(W):
                    if (row>>i)&1 or (column>>j)&1:
                        tmp[i][j] = 'r'
                    else:
                        tmp[i][j] = c[i][j]
            s = 0
            for i in range(H):
                for j in range(W):
                    if tmp[i][j] == '#':
                        s += 1
            if s == K:
                cnt += 1
    
    print(cnt)


if __name__ == '__main__':
    main()

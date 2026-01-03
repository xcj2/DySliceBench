import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    W, H, N = mi()
    p = [[0]*W for _ in range(H)]
    for i in range(N):
        xi, yi, ai = mi()
        if ai == 1:
            for x in range(xi):
                for y in range(H):
                    p[y][x] = 1
        if ai == 2:
            for x in range(xi, W):
                for y in range(H):
                    p[y][x] = 1
        if ai == 3:
            for x in range(W):
                for y in range(yi):
                    p[y][x] = 1
        if ai == 4:
            for x in range(W):
                for y in range(yi, H):
                    p[y][x] = 1
    print(W*H-sum(sum(p[i]) for i in range(H)))

if __name__ == '__main__':
    main()

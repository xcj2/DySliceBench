# 幅優先探索（行きがけ）
import collections
import sys
import math


def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def main():
    N = I()
    if N <= 5:
        for i in range(N):
            print(0)
        return

    def yy(x, y, z):
        return x**2+y**2+z**2+x*y+y*z+z*x

    for i in range(5):
        print(0)

    for i in range(6, N+1):
        cn = 0
        n = math.floor(math.sqrt(i)+1)
        start = math.floor(math.sqrt(i/6))
        for j in range(start, n):
            if j**2 >= i-4:
                break
            for k in range(1, j+1):
                if j**2+k**2+j*k >= i-2:
                    break
                for l in range(1, k+1):
                    y = yy(j, k, l)
                    if y > i:
                        break
                    if y == i:
                        if j == k == l:
                            cn += 1
                        elif j != k != l:
                            cn += 6
                        else:
                            cn += 3
        print(cn)


if __name__ == '__main__':
    main()

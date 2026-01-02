import sys
import math

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    f = [0]*(n+1)
    n_sqrt = int(math.sqrt(n))
    for x in range(1, n_sqrt):
        for y in range(x, n_sqrt):
            for z in range(y, n_sqrt):
                cnt = 0
                if x == y == z:
                    cnt = 1
                elif x != y != z:
                    cnt = 6
                else:
                    cnt = 3
                idx = x*x + y*y + z*z + x*y + y*z + z*x
                if idx <= n:
                    f[idx] += cnt
    ans = '\n'.join(str(v) for v in f[1:n+1])
    print(ans)

if __name__ == '__main__':
    main()
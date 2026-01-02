import sys
from bisect import bisect_right, bisect_left
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    C = list(map(int, readline().split()))
    A.sort()
    B.sort()
    C.sort()
    ans = 0
    for i in range(N):
        top = bisect_left(A, B[i])
        bottom = bisect_right(C, B[i])
        if top>0 and bottom != N:
            ans += top*(N-bottom)
    print(ans)
if __name__ == '__main__':
    main()
import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    _LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    n,q = LI()
    bit = [0] * (n+1)

    def bit_add(i,x):
        while i <= n:
            bit[i] += x
            i += i & (-i)

    def sum_bit(i):
        ret = 0
        while i > 0:
            ret += bit[i]
            i -= i & (-i)
        return ret

    for _ in range(q):
        c,x,y = LI()
        if c == 0:
            bit_add(x,y)
        else:
            ans = sum_bit(y) - sum_bit(x-1)
            print(ans)


if __name__ == '__main__':
    main()

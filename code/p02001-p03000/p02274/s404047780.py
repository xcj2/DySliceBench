import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    n = NI()
    A = LI()
    S = sorted(A)

    bit = [0] * (n+1)

    def bit_add(i,x):
        while i <= n:
            bit[i] += x
            i += i & (-i)

    def bit_sum(i):
        ret = 0
        while i > 0:
            ret += bit[i]
            i -= i & (-i)
        return ret

    ans = 0
    for i,x in enumerate(A):
        z = bisect.bisect_left(S,x) + 1
        bit_add(z,1)
        ans += z - bit_sum(z)
    print (ans)

if __name__ == '__main__':
    main()

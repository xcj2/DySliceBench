import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    n = NI()
    bit = [0] * (n+1)

    def add(i,x):
        while i <= n:
            bit[i] += x
            i += i & -i

    def query(i):
        x = 0
        while i > 0:
            x += bit[i]
            i -= i & -i
        return x

    for i,a in enumerate(LI()):
        add(i+1,int(a))

    ans = INF

    b = [bit,copy.copy(bit)]
    for s in (1,-1):
        bit = b[(s+1)//2]
        cnt = 0
        x = s
        for i in range(1,n+1):
            z = query(i)
            if z * x <= 0:
                add(i,x-z)
                cnt += abs(x-z)
            x = -x
        ans = min(ans,cnt)
    print(ans)


if __name__ == '__main__':
    main()
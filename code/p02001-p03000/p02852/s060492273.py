import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**5 + 1
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,M = LI()
    S = SI()
    N0 = 2 ** N.bit_length()
    st = [INF] * (2*N0)

    def update(i,x):
        i += N0-1
        st[i] = x
        while i > 0:
            i = (i-1) // 2
            st[i] = min(st[i*2+1], st[i*2+2])

    def query(l,r):
        L = l+N0; R = r+N0
        ret = INF
        while L < R:
            if L % 2:
                ret = min(ret,st[L-1])
                L += 1
            if R % 2:
                R -= 1
                ret = min(ret,st[R-1])
            L //= 2; R //= 2
        return ret

    update(0,0)

    for i in range(1,N+1):
        if S[i] == '1': continue
        else:
            if i <= M:
                update(i,1)
            else:
                x = query(i-M,i)
                update(i,x+1)
    if st[N+N0-1] >= INF:
        print(-1)
    else:
        ans = []
        f = N
        last_i = N
        s = st[N+N0-1]
        d = 1
        cnt = 0
        for i in range(N-1,-1,-1):
            cnt += 1
            if st[i+N0-1] == s-1:
                d = f - i
                last_i = i
            if cnt == M:
                ans.append(d)
                f = last_i
                s -= 1
                cnt = f - i
        if f > 0:
            ans.append(f)
        print(*reversed(ans),sep=' ')

if __name__ == '__main__':
    main()
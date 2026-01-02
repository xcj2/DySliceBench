import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,K = LI()
    P = LI()

    N0 = 2 ** (N.bit_length())
    st1 = [0] * (2 * N0)
    st2 = [0] * (2 * N0)

    i = N0-1
    for x in P:
        st1[i] = st2[i] = x
        i += 1


    for i in range(N0-2,-1,-1):
        st1[i] = max(st1[i*2+1],st1[i*2+2])
        st2[i] = min(st2[i*2+1],st2[i*2+2])

    def query_max(l, r):
        L = l + N0;
        R = r + N0
        ret = 0
        while L < R:
            if L % 2:
                ret = max(ret, st1[L - 1])
                L += 1
            if R % 2:
                R -= 1
                ret = max(ret, st1[R - 1])
            L //= 2;
            R //= 2
        return ret


    def query_min(l, r):
        L = l + N0;
        R = r + N0
        ret = N + 1  # max value
        while L < R:
            if L % 2:
                ret = min(ret, st2[L - 1])
                L += 1
            if R % 2:
                R -= 1
                ret = min(ret, st2[R - 1])
            L //= 2;
            R //= 2
        return ret


    ans = 0
    cnt = 0
    flg = 0
    bp = N
    for i in range(N):
        if P[i] > bp:
            cnt += 1
        else:
            cnt = 0
        bp = P[i]

        if i < K - 1: continue

        if cnt >= K-1:
            flg = 1
        elif i >= K and query_min(i-K,i) == P[i-K] and query_max(i-K+1,i+1) == P[i]:
            pass
        else:
            ans += 1

    print(ans+flg)


if __name__ == '__main__':
    main()
import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    a = [(int(x),i+1) for i,x in enumerate(sys.stdin.readline().split())]

    N0 = 2**(N.bit_length())
    st1 = [0] * (2*N0)
    st2 = [N+1] * (2*N0)

    def update_max(i,x):
        i += N0 - 1
        st1[i] = x
        while i > 0:
            i = (i-1) // 2
            st1[i] = max(st1[i*2+1],st1[i*2+2])

    def update_min(i,x):
        i += N0 - 1
        st2[i] = x
        while i > 0:
            i = (i-1) // 2
            st2[i] = min(st2[i*2+1],st2[i*2+2])

    def query_max(l,r):
        L = l + N0; R = r + N0
        ret = 0
        while L < R:
            if L % 2:
                ret = max(ret,st1[L-1])
                L += 1
            if R % 2:
                R -= 1
                ret = max(ret,st1[R-1])
            L //= 2; R //=2
        return ret

    def query_min(l,r):
        L = l + N0; R = r + N0
        ret = N+1
        while L < R:
            if L % 2:
                ret = min(ret,st2[L-1])
                L += 1
            if R % 2:
                R -= 1
                ret = min(ret,st2[R-1])
            L //= 2; R //= 2
        return ret

    a.sort()
    ans = 0
    for x,y in a:
        i = query_max(1,y)
        j = query_min(y,N+1)
        ans += (y-i) * (j-y) * x
        update_max(y,y)
        update_min(y,y)

    print(ans)


if __name__ == '__main__':
    main()
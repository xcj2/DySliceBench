import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()

    N0 = 2**(N.bit_length())
    st = [0] * (N0*2)

    def gindex(l, r):
        L = l + N0; R = r + N0
        lm = (L // (L & -L)) // 2
        rm = (R // (R & -R)) // 2
        while L < R:
            if R <= rm:
                yield R - 1
            if L <= lm:
                yield L - 1
            L //= 2; R //= 2
        while L > 0:
            yield L - 1
            L //= 2

    def update(i,s):
        x = 2 ** (ord(s) - ord('a'))
        i += N0-1
        st[i] = x
        while i > 0:
            i = (i-1) // 2
            st[i] = st[i*2+1] | st[i*2+2]

    def query(l,r):
        l += N0
        r += N0
        ret = 0

        while l < r:
            if l % 2:
                ret |= st[l-1]
                l += 1
            if r % 2:
                r -= 1
                ret |= st[r-1]
            l //= 2 ; r //= 2

        return ret


    for i,s in enumerate(sys.stdin.readline().rstrip()):
        update(i+1,s)
    Q = NI()
    for _ in range(Q):
        c,a,b = sys.stdin.readline().split()
        if c == '1':
            update(int(a),b)
        else:
            ret = query(int(a),int(b)+1)
            cnt = 0
            b = 1
            for i in range(26):
                cnt += (b & ret) > 0
                b <<= 1
            print(cnt)


if __name__ == '__main__':
    main()
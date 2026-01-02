import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()

    R = 2**(N.bit_length())
    st = [0] * (R*2)

    def update(i,s):
        x = 2 ** (ord(s) - ord('a'))
        i += R-1
        st[i] = x
        while i > 0:
            i = (i-1) // 2
            st[i] = st[i*2+1] | st[i*2+2]

    def query(l,r):
        l += R-1
        r += R-2
        ret = 0

        while l+1 < r:
            if l % 2 == 0:
                ret |= st[l]
            if r % 2 == 1:
                ret |= st[r]
                r -= 1
            l = l // 2
            r = (r-1) // 2
        if l == r:
            ret |= st[l]
        else:
            ret |= st[l] | st[r]

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
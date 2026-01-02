import sys

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    n,q = LI()

    n0 = 2**((n-1).bit_length())
    st = [2**31-1] * (n0*2)

    def find(s,t):
        s += n0; t += n0
        ret = 2**31 - 1
        while s < t:
            if s % 2:
                ret = min(ret,st[s-1])
                s += 1
            if t % 2:
                t -= 1
                ret = min(ret,st[t-1])
            s >>= 1; t >>= 1
        return ret

    def update(i,x):
        i += n0 - 1
        st[i] = x
        while i > 0:
            i = (i-1) // 2
            st[i] = min(st[i*2+1],st[i*2+2])

    for _ in range(q):
        c,x,y = LI()
        if c == 0:
            update(x,y)
        else:
            print(find(x,y+1))


if __name__ == '__main__':
    main()

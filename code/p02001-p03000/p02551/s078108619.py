import sys,queue,math,copy,itertools,bisect,collections,heapq



def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N, Q = LI()

    N0 = 2 ** (N-1).bit_length()

    stx = [N-1] * (N0*2)
    sty = [N-1] * (N0*2)

    def update(l,r,x,st):
        l += N0 - 1
        r += N0 - 1
        while l < r:
            st[l] = min(st[l],x)
            st[r] = min(st[r],x)

            l //= 2
            r = r // 2 - 1

        st[l] = min(st[l],x)

    def get_data(i,st):
        i += N0-1
        ret = N-1
        while i >= 0:
            ret = min(ret,st[i])
            i = (i-1) // 2
        return ret


    ans = (N-2) ** 2
    for _ in range(Q):
        c,p = LI()
        p -= 1
        if c == 1:
            s = get_data(p,sty)
            ans -= s - 1
            update(0,s-1,p,stx)
        else:
            s = get_data(p,stx)
            ans -= s - 1
            update(0,s-1,p,sty)

    print(ans)
if __name__ == '__main__':
    main()
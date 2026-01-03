import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    INF = float('inf')
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,x = LI()
    a = LI()

#    N0 = 2**(N.bit_length())
#    st = [INF] * (2*N0)

    def update(i,x):
        i += N0-1
        st[i] = x
        while i > 0:
            i = (i-1) // 2
            st[i] = min(st[i*2+1],st[i*2+2])

    def query(l,r):
        l += N0; r += N0
        ret = INF
        while l < r:
            if l % 2:
                ret = min(ret,st[l-1])
                l += 1
            if r % 2:
                r -= 1
                ret = min(ret,st[r-1])
            l >>= 1; r >>= 1
        return ret

#    for i,j in enumerate(a):
#        update(i,j)
    min_a = copy.copy(a)

    ans = INF
    for i in range(N):
        tmp = i * x
        for j in range(N):
            l = j - i
            min_a[j] = min(min_a[j],a[l])
            tmp += min_a[j]
        ans = min(ans,tmp)
    print(ans)




if __name__ == '__main__':
    main()
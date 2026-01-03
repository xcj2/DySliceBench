import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,_ = LI()
    N0 = 2 ** N.bit_length()
    st = [0] * (N0*2)

    def add(p,x):
        p += N0-1
        st[p] = x
        while p > 0:
            p = (p-1) // 2
            st[p] = max(st[p*2+1],st[p*2+2])

    def get(a,b,x,l,r):
        if a <= l and r <= b: return st[x]
        if a >= r or b <= l: return 0
        vl = get(a,b,x*2+1,l,(l+r)//2)
        vr = get(a,b,x*2+2,(l+r)//2,r)
        return max(vl,vr)

    A = []
    for e,a in enumerate(sys.stdin.readline().split()):
        a = int(a)
        A.append(a)
        add(e+1,a)
    max_a = -1
    max_cnt = 0
    for i in range(1,N):
        a = get(i+1,N+1,0,0,N0) - A[i-1]
        if a > max_a:
            max_a = a; max_cnt = 1
        elif a == max_a:
            max_cnt += 1

    print(max_cnt)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    def binsearch_left(a, x):
        l = -1
        r = len(a)
        while r-l>1:
            m = (l+r)//2
            if x<a[m]:
                r = m
            else:
                l = m
        return r

    def binsearch_right(a, x):
        l = -1
        r = len(a)
        while r-l>1:
            m = (l+r)//2
            if x<=a[m]:
                r = m
            else:
                l = m
        return r

    ans = 0
    for b in B:
        a_r = binsearch_right(A, b)
        c_l = binsearch_left(C, b)
        ans += a_r * (N - c_l)

    print(ans)

if __name__ == '__main__':
    resolve()

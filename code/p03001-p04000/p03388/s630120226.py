import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


def g(c):  # i*(i+1) <= c たる最大のiを返す
    left = 0  # ok
    right = c  # ng
    while left + 1 < right:
        mid = (left + right)//2
        if mid*(mid+1) <= c:
            left = mid
        else:
            right = mid
    return left


def query(a,b):
    if a == b:
        return a+b-2
    if a > b:
        a,b = b,a
    i0 = g(a*b)
    return i0+(a*b-1)//(i0+1)-1


Q = I()
for i in range(Q):
    a,b = MI()
    print(query(a,b))

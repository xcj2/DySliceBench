def add(i, x):
    i += n-1
    sg[i] += x
    while i>0:
        i = (i-1)//2
        sg[i] += x


def getSum(a, b):
    return _getSum(a, b+1, 0, 0, n)


def _getSum(a, b, k, l, r):
    if b <= l or r <= a:
        return 0

    if a <= l and r <= b:
        return sg[k]

    ll = _getSum(a, b, k*2+1, l, (r+l)/2)
    rr = _getSum(a, b, k*2+2, (r+l)/2, r)
    return ll+rr


(_n, q) = map(int, input().split())
n=1
while n <= _n:
    n*=2

sg = [0] * (2*n-1)

for i in range(q):
    (c, x, y) = map(int, input().split())
    if c:
        print(getSum(x, y))
    else:
        add(x, y)
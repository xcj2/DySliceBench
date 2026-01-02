K = int(input())
A = list(map(int, input().split()))

def winner_count(N, A=A):
    for a in A:
        N = a*(N//a)
    return N

def bisect_left(func, l, r, target):
    # n>=i ⇒ func(n) <= targetを満たす最小のi
    # l=1, r=sum(A)+2
    # func(l)<= target, target<=func(r)
    if l==r:
        return 0
    if l+1==r:
        if func(l)< target:
            return r
        else:
            return l
    c = (l+r)//2
    if target <= func(c):
        return bisect_left(func, l, c, target)
    else:
        return bisect_left(func, c, r, target)

def bisect_right(func, l,r, target):
    if l==r:
        return 0
    if l+1==r:
        if target < func(r):
            return l
        else:
            return r
    c = (l+r)//2
    if target < func(c):
        return bisect_right(func, l, c, target)
    else:
        return bisect_right(func, c, r, target)

_min = bisect_left(winner_count, 1, sum(A)+2, 2)
_max = bisect_right(winner_count, 1, sum(A)+2, 2)


if _min > _max:
	print(-1)
else:
	print(_min, _max)
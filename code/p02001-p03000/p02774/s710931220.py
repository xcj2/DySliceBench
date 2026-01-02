from bisect import bisect_right, bisect_left

N,K = map(int,input().split())
A = sorted(map(int,input().split()))

t0 = bisect_left(A,0)
t1 = bisect_right(A,0)
pos = A[t1:]
neg = [-v for v in reversed(A[:t0])]
zeros = t1-t0
offset_negative = len(pos)*len(neg)
offset_zero = zeros*(N-zeros) + zeros*(zeros-1)//2
offset = offset_zero + offset_negative

def bisect2(ng, ok, judge):
    while abs(ng-ok) > 1:
        m = (ng+ok)//2
        if judge(m):
            ok = m
        else:
            ng = m
    return ok

def count1(l,n):
    j = len(l)
    cnt = 0
    for i,a in enumerate(l):
        v = n//a
        while j > i and l[j-1] > v:
            j -= 1
        if j <= i:
            break
        else:
            cnt += j-i-1
    return cnt

def count2(l1,l2,n):
    j = len(l2)
    cnt = 0
    for i,a in enumerate(l1):
        v = n//a
        while j > 0 and l2[j-1] > v:
            j -= 1
        cnt += j
    return cnt


def cnt(n):
    if n > 0:
        cnt = count1(pos,n-1) + count1(neg,n-1) + offset
    else:
        cnt = offset_negative - count2(pos,neg,-n)
    return cnt


if offset_negative < K <= offset:
    print(0)
else:
    temp = max(abs(a) for a in A)**2
    print(bisect2(temp, -temp, lambda n: cnt(n) <= K-1))

# from itertools import combinations
# s = sorted(a*b for a,b in combinations(A,2))
# for i,v in enumerate(s):
#     print(cnt(v),i,v)
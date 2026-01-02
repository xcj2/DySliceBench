def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
# import bisect

N = INT()
A = LIST()
B = LIST()
C = LIST()

A.sort()
B.sort()
C.sort()

def binsearch(lst, th, ud="up"):
    left, right = -1, len(lst)
    while right - left > 1:
        mid = (left + right) // 2
        if ud == "up":
            if lst[mid] > th:
                right = mid
            else:
                left = mid
        else:
            if lst[mid] >= th:
                right = mid
            else:
                left = mid
        
    return right if ud == "up" else left


ans = 0
# for ai in A:
#     i = bisect.bisect_right(B, ai)
#     for bi in B[i:]:
#         j = bisect.bisect_right(C, bi)
#         ans += len(C[j:])

for bi in B:
    i = binsearch(A, bi, "down")
    j = binsearch(C, bi, "up")
    ans += (i+1) * (N-j)


print(ans)
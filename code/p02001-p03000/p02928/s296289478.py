from collections import Counter
mod = 1000000007


def inverse(a):
    return pow(a, mod - 2, mod)


def usearch(x, a):
    lft = 0
    rgt = len(a) + 1
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if a[mid] <= x:
            lft = mid
        else:
            rgt = mid
    return lft


def bubble_sort(A):
    cnt = 0
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                cnt += 1
    return cnt

def main():
    n, k=map(int, input().split())
    a = list(map(int, input().split()))
    ans = bubble_sort(a) * k % mod
    div2 = inverse(2)
    # a.sort()
    lft = 0
    rgt = 0
    while lft < n:
        while rgt < n and a[lft] == a[rgt]:
            rgt += 1
        ans = (ans + (rgt - lft) * (n - rgt) % mod * k % mod * (k-1) * div2 % mod) % mod
        lft =rgt

    print(ans)
main()

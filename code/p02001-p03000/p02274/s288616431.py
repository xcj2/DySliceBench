
def merge(ns, ns1, ns2, n, mid):
    j = 0
    k = 0
    c = 0
    for i in range(n):
        if ns1[j] < ns2[k]:
            ns[i] = ns1[j]
            j += 1
            if j == mid:
                for l in range(n - mid - k):
                    ns[i + 1 + l] = ns2[k + l]
                return c
        else:
            ns[i] = ns2[k]
            k += 1
            c += mid - j
            if k == n - mid:
                for l in range(mid - j):
                    ns[i + 1 + l] = ns1[j + l]
                return c

def merge_sort(ns, n):
    if n <= 1:
        return 0
    elif n == 2:
        if ns[0] > ns[1]:
            k = ns[0]
            ns[0] = ns[1]
            ns[1] = k
            return 1
        else:
            return 0
    else:
        mid = n // 2
        ns1 = ns[:mid]
        ns2 = ns[mid:]
        c1 = merge_sort(ns1, mid)
        c2 = merge_sort(ns2, n - mid)
        c3 = merge(ns, ns1, ns2, n, mid)
        return c1 + c2 + c3

def compute_inversions(ns, n):
    return merge_sort(ns, n)

n = int(input())
ns = list(map(int, input().split()))

print(compute_inversions(ns, n))
# Quick Sort #
def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for k in range(p, r):
        if A[k][1] <= x:
            i += 1
            A[i], A[k] = A[k], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def bubble_sort(c, n):
    x = c[:]
    for i in range(n):
        for k in range(n-1, i, -1):
            if x[k][1] < x[k-1][1]:
                x[k], x[k-1] = x[k-1], x[k]
    return x

def is_stable(_in, out):
    n = len(_in)
    for i in range(n):
        for k in range(i+1, n):
            for a in range(n):
                for b in range(a+1, n):
                    if _in[i][1] == _in[k][1] and _in[i] == out[b] and _in[k] == out[a]:
                        return False
    return True

n = int(input())
a = []
for i in range(n):
    mrk, num = input().split()
    num = int(num)
    a.append((mrk, num))
b = a[:]
quick_sort(b, 0, n-1)
if n > 10000:
    print("Not stable")
else:
    c = bubble_sort(a[:], n)
    if b == c:
        print("Stable")
    else:
        print("Not stable")
for i in b:
    print(*i)

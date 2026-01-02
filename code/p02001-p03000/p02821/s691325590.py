n,m = map(int, input().split())
A = sorted(list(map(int, input().split())),reverse=True)

def cnt(x):
    c = 0
    i = 0
    for j in reversed(range(len(A))):
        while i <n and A[j]+A[i]>=x:
            i += 1
        c += i
    return c

def happiness(x):
    c = 0
    i = 0
    ci = 0
    for j in reversed(range(len(A))):
        while i <n and A[j]+A[i]>=x:
            ci += A[i]
            i += 1
        c += ci + A[j]*i
    return c

def binary_search(l, r):
    mid = (l+r)//2
    c = cnt(mid)
    if c < m:
        return binary_search(l, mid)   
    else:
        if l == mid:
            return(l, c-m)
        return binary_search(mid, r)

x, dm = binary_search(0, A[0]*2+1)
print(happiness(x)-dm*x)
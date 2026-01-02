
def calc(N, A, i):
    x = 0
    r = 0
    for j, a in enumerate(A):
        if j == i:
            continue
        r += abs(x - a)
        x = a
    r += abs(x)
    return r

def calc0(N, A):
    x = 0
    r = 0
    for a in A:
        r += abs(x - a)
        x = a
    return r

def calc1(N, A, ra, i):
    x0 = A[i - 1]
    x1 = A[i]
    x2 = A[i + 1]
    return ra - abs(x0 - x1) - abs(x1 - x2) + abs(x0 - x2)

#N = 1000
#A = list(range(N))

N = int(input())
A = [int(_) for _ in input().split()]
A += [0]

ra = calc0(N, A)

for i in range(N):
    print(calc1(N, A, ra, i))

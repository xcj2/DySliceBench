from collections import defaultdict
inpl = lambda: list(map(int,input().split()))

N, Q = inpl()
S = input()
T = []
D = []
for i in range(Q):
    t,d = input().split()
    T.append(t)
    D.append(d)

finalposmem = defaultdict(lambda: None)
def finalpos(i):
    if i < 0:
        return -1
    elif i >= N:
        return 1

    for q in range(Q):
        if S[i] == T[q]:
            if D[q] == 'L':
                i -= 1
            else:
                i += 1
            if i < 0:
                return -1
            elif i >= N:
                return 1
    return 0

def finalpos_withmem(i):
    mem = finalposmem[i]
    if mem is None:
        z = finalpos(i)
        finalposmem[i] = z
        return z
    else:
        return mem

def bisect_left_withkey(a, x, key=lambda x: x):
    right = len(a)
    left = 0
    kx = key(x)
    while left + 1 < right:
        new = (left + right)//2
        kn = key(a[new])
        if kx <= kn:
            right = new
        else:
            left = new
    return right

def bisect_right_withkey(a, x, key=lambda x: x):
    right = len(a)
    left = 0
    kx = key(x)
    while left + 1 < right:
        new = (left + right)//2
        kn = key(a[new])
        if kx < kn:
            right = new
        else:
            left = new
    return right

right_bound = bisect_left_withkey(range(N),N,key=finalpos_withmem)
left_bound = bisect_right_withkey(range(N),-1,key=finalpos_withmem)
right_killed = N - right_bound
left_killed = left_bound
killed = left_killed + right_killed
ans = N - killed

print(ans)
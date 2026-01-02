def inpl(): return list(map(int, input().split()))

N, Q = inpl()
S = input()
T = [""]*(Q)
D = [-1]*(Q)
for i in range(Q):
    t, d = input().split()
    T[i] = t
    D[i] += 2*(d == "R")

def checkL(ix):
    for i in range(Q):
        if T[i] == S[ix]:
            ix += D[i]
        if ix == N:
            return True
        if ix < 0:
            return False
    return True

def checkR(ix):
    for i in range(Q):
        if T[i] == S[ix]:
            ix += D[i]
        if ix == N:
            return False
        if ix < 0:
            return True
    return True

OK = N
NG = -1
while abs(OK-NG)>1:
    mid = (OK+NG)//2
    if checkL(mid):
        OK = mid
    else:
        NG = mid

Lans = OK*1

OK = -1
NG = N
while abs(OK-NG)>1:
    mid = (OK+NG)//2
    if checkR(mid):
        OK = mid
    else:
        NG = mid
print(max(OK-Lans+1, 0))
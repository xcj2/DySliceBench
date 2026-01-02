def sim(i):
    for t, d in qs:
        if S[i] == t:
            div = 1 if d == "R" else -1
            i += div
            if i == 0:
                return 0
            elif i == N+1:
                return N+1
    return i

def bin_search_left():
    ok = 0
    ng = N+1

    while abs(ok-ng)>1:
        mid = (ok+ng) //2
        res = sim(mid)
        #print(ok,ng,mid,res)
        if res == 0:
            ok = mid
        if res >0:
            ng = mid
    return ok


def bin_search_right():
    ng = 0
    ok = N+1

    while abs(ok-ng)>1:
        mid = (ok+ng) //2
        res = sim(mid)
        #print(ok,ng,mid,res)
        if res < N+1:
            ng = mid
        if res >= N+1:
            ok = mid
    return ok


N, Q = map(int,input().split())
S = "0"+input()+"0"
qs = []
for _ in range(Q):
    t, d = input().split()
    qs.append((t,d))

L = bin_search_left()
R = bin_search_right()
print(N-L-(N+1-R))
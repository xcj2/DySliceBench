from functools import reduce

INF = 10**9+1

N,M = map(int,input().split())
A = list(map(int,input().split(" ")))

def GCD(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return GCD(b,a%b)

def LCM(a,b):
    return a*b//GCD(a,b)

def LCM_list(L):
    return reduce(LCM,L)

B = [A[i]//2 for i in range(N)]
flag = False
for i in range(N-1):
    count,count_,b,b_ = 0,0,B[i],B[i+1]
    while b % 2 == 0:
        b //= 2
        count += 1
    while b_ % 2 == 0:
        b_ //= 2
        count_ += 1
    if count != count_:
        flag = True
        print(0)
        exit()

hlcm = LCM_list(B)
if hlcm <= M:
    lb,ub = 1,INF
    while lb < ub:
        mid = (lb + ub) // 2
        if hlcm * mid <= M and hlcm * (mid+1) > M:
            break
        elif hlcm * mid > M:
            ub = mid
        else:
            lb = mid
    ans = (mid+1)//2
    print(ans)
else:
    print(0)

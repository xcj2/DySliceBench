#template
def inputlist(): return [int(k) for k in input().split()]
def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)
#10->n(sinhou)
def len_check(k,n):
    if len(k) == n:
        return k
    else:
        for _ in range(n-len(k)):
            k = '0'+k
        return k
#template
N,M,X = inputlist()
li = [0]*N
cost = 10**9
for i in range(N):
    li[i] = inputlist()
for k in range(2**N):
    ans = [0]*M
    k = len_check(base10to(k,2),N)
    lis = []
    tmp = 0
    count = 0
    for i in range(N):
        if k[i] == '1':
            lis.append(li[i])
    n = len(lis)
    for i in range(n):
        tmp += lis[i][0]
        alg = lis[i][1:]
        for j in range(M):
            ans[j] += alg[j]
    for i in range(M):
        if ans[i] >= X:
            count+=1
    if count == M:
        cost = min(cost,tmp)

if cost == 10**9:
    print(-1)
else:
    print(cost)
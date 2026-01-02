#template
def inputlist(): return [int(k) for k in input().split()]
def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)
def len_check(k,n):
    if len(k) == n:
        return k
    else:
        for _ in range(n-len(k)):
            k = '0'+k
        return k
#template
D,G = inputlist()
ans = 10**9
li = [0]*D
for i in range(D):
    li[i] = inputlist()
for i in range(2**D):
    lis = []
    k = base10to(i,2)
    k = len_check(k,D)
    for d in range(D):
        if k[d] == '1':
            otake = [(d+1)*100] + li[d]
            lis.append(otake)
    lis.sort(reverse=True)
    n = len(lis)
    tmp = 0
    count = 0
    for t in range(n):
        p = lis[t][1]
        point = lis[t][0]
        for pt in range(1,p+1):
            tmp += point
            count +=1
            if pt == p:
                tmp += lis[t][2]
            if tmp >= G:
                ans = min(ans,count)
                break
print(ans)
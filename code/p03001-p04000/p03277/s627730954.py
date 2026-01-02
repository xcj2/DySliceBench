N=int(input())
A=list(map(int,input().split()))

def median(num):
    row=[0]*N
    for i in range(N):
        if A[i]>num:
            row[i]=1
        else:
            row[i]=-1
    m=0
    data=[0]
    for i in range(0,N):
        data.append(data[-1]+row[i])
        m=min(m,data[i+1])
    data=[data[i]-m+1 for i in range(N+1)]
    ans=0
    BIT=[0]*(N+2)
    n=N+1
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    def BIT_update(idx,x):
        while idx <= n:
            BIT[idx] += x
            idx += idx&(-idx)
        return

    for i in range(0,N+1):
        val=data[i]
        ans+=BIT_query(val)
        BIT_update(val,1)
    test=N*(N+1)//2-ans
    return test>=((N*(N+1)//2)//2+1)

start=0
end=10**9
while end-start>1:
    test=(end+start)//2
    if median(test):
        end=test
    else:
        start=test

if median(start):
    print(start)
else:
    print(end)
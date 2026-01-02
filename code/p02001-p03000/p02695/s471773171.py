import math
def facts(n):
    ans = []
    for  i in range(1, int(math.sqrt(n)+1)):
        if(n%i==0):
            ans.append(i)
            ans.append(n//i)
    ans = sorted(ans)
    return ans


n,m,q =map(int, input().split())
qs = []
ans = 0
for i in range(q):
    arr= list(map(int, input().split()))
    qs.append(arr)
    
def calc(x):
    global ans
    tmp = 0
    for i in range(q):
        if(x[qs[i][1]-1]-x[qs[i][0]-1]==qs[i][2]):
            tmp+=qs[i][3]
    ans = max(ans, tmp)

def dfs(x):
    if(len(x)==n):
        calc(x)
    else:
        for i in range(x[-1], m+1):
            x.append(i)
            dfs(x)
            x.pop()
dfs([1])
print(ans)

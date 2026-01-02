n,m,k = (int(num) for num in input().split())
f_l = [0] * n
b_l = [[] for _ in range(n)]
par = [i for i in range(n)]
rank = [0] * n
size = [1] * n

def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])
        
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif rank[x] < rank[y]:
        par[x] = y
        size[y] += size[x]
    else:
        par[y] = x
        size[x] += size[y]
        if rank[x] == rank[y]:
            rank[x] += 1
    return
            
def isSame(x,y):
    return find(x) == find(y)

for _ in range(m):
    a,b = (int(num) for num in input().split())
    a -= 1
    b -= 1
    f_l[a] += 1
    f_l[b] += 1
    unite(a,b)
    #print("par:  ", par)
    #print("rank: ", rank)
    
for _ in range(k):
    a,b = (int(num) for num in input().split())
    a -= 1
    b -= 1
    b_l[a].append(b)
    b_l[b].append(a)
    
ans = ""

for i in range(n):
    ans_num = size[find(i)] - f_l[i] -1
    for num in b_l[i]:
        if isSame(i,num):
            ans_num -= 1
    ans_num = max(ans_num,0)
    ans += str(ans_num) + " "
    
print(ans)
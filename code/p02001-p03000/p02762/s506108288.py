import sys
sys.setrecursionlimit(100000)

N,M, K = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(M)]
CD = [list(map(int,input().split())) for i in range(K)]


#xの木の根を求める
def root(x,li): 
    if li[x] == x:
        return x
    else:
        li[x] = root(li[x],li)
        return li[x]

#xとyが同じ集合に属するかの判定
def find(x,y,li):
    return root(x,li) == root(y,li)

#xとｙを併合
def union(x,y,li):
    x = root(x,li)
    y = root(y,li)
    if x==y:
        return
    else:
        li[x]=y

li1 = [i for i in range(N)]
li2 = [i for i in range(N)]

for i in range(M):
    a = AB[i][0]
    b = AB[i][1]
    # print(str(i)+" ",end="")
    union(min(a-1,b-1),max(a-1,b-1),li1)
# for i in range(K):
#     c = CD[i][0]
#     d = CD[i][1]
#     union(c-1,d-1,li2)

mm = [0 for i in range(max(li1)+1)]
for i in range(N):
    m = root(i,li1)
    mm[m] += 1

# print(li1)
# print(mm)
ans = [mm[li1[i]]-1 for i in range(N)]
# print(ans)

for i in range(M):
    a = AB[i][0]
    b = AB[i][1]
    ans[a-1] -= 1
    ans[b-1] -= 1


for i in range(K):
    c = CD[i][0]
    d = CD[i][1]
    if find(c-1,d-1,li1):
        ans[c-1] -= 1
        ans[d-1] -= 1
print(*ans)




import collections
import sys
sys.setrecursionlimit(10**6)

def getls():
    return [ipt for ipt in input().split()]
def getlsi():
    return [int(ipt) for ipt in input().split()]
#Topological sort Gは辞書として渡す
def tsort(N,G,dic):
    res = 0
    #Topological Sort
    if dic[N] != -1:
        return dic[N]
    for node in G[N]:
        res = max(res,tsort(node,G,dic)+1)
    dic[N] = res
    return dic[N]

[n,m] = getlsi()
dic_next = collections.defaultdict(list)
dp = [-1] * n
for i in range(m):
    [x,y] = getlsi()
    dic_next[x-1].append(y-1)
ans = 0
for i in range(n):
    ans = max(ans,tsort(i,dic_next,dp))
print(ans)

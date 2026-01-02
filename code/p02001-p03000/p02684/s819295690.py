#template
def inputlist(): return [int(k) for k in input().split()]
import sys
sys.setrecursionlimit(10**6)
#template
N,K = inputlist()
A = inputlist()
seen = [False]*(N+1)
dic = {n:0 for n in range(1,N+1)}
for i in range(N):
    dic[i+1] = A[i]

def search(i,count):
    seen[i] = True
    next_i = dic[i]
    if seen[next_i]:
        count+=1
        return [next_i,count]
    count+=1
    return search(next_i,count)
key,count_sum = search(1,0)

def find(i,count):
    if i == key:
        return count
    count+=1
    return find(dic[i],count)

tmp = find(1,0)
if K < count_sum:
    ans = 1
    for i in range(K):
        ans = dic[ans]
    print(ans)
    exit()

d = count_sum-tmp
Ka = K-tmp

mod = Ka % d

loop = []
loop.append(key)
def dfs(i):
    next_i = dic[i]
    if next_i == key:
        return False
    loop.append(next_i)
    return dfs(next_i)
dfs(key)

print(loop[mod])

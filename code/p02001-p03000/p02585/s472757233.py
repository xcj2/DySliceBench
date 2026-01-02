def find(vals,l):
    ans = -float('inf')
    for i in range(len(vals)//2):
        curr = vals[i+l-1]
        if i-1 >= 0:
            curr -= vals[i-1]

        ans = max(ans,curr)

    #print(ans,l)
    return ans

def dfs(edges,node,k,costs,visited):
    nodes = []
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            nodes.append(node)
            stack.append(edges[node])

    vals = []
    for node in nodes:
        vals.append(costs[node-1])

    vals.extend(vals)
    for i in range(1,len(vals)):
        vals[i] += vals[i-1]

    total = vals[-1]//2
    if total >= 0:
        ans = total*(k//(len(vals)//2))
    else:
        ans = 0

    max_val = -float('inf')
    #print('here',len(vals)//2,total)
    val = -float('inf')
    if k >= len(vals)//2:
        for i in range(1,len(vals)//2+1):
            max_val = max(max_val,find(vals,i))

        if total >= 0:
            max_val += ans-total

    #print(max_val)
    val = -float('inf')
    #print(total)
    k %= (len(vals)//2)
    
    for i in range(1,k+1):
        val = max(val,find(vals,i))

    return max(max_val,ans+val)

def main():
    n,k = map(int,input().split())
    perm = list(map(int,input().split()))
    costs = list(map(int,input().split()))
    edges = [-1]*(n+1)
    for i in range(n):
        edges[i+1] = perm[i]

    ans = -float('inf')
    visited = set()
    for i in range(1,n+1):
        if i not in visited:
            ans = max(ans,dfs(edges,i,k,costs,visited))

    print(ans)

main()

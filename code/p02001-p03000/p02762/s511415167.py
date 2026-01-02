def dfs(node,visited,friends,connected_compnts):
    cmpnt = set()
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            cmpnt.add(curr)
            for kid in friends[curr]:
                stack.append(kid)

    connected_compnts.append(cmpnt)

def solve(cmpnt,friends,blocks,ans):
    arr = list(cmpnt)
    for node in arr:
        cmpnt.remove(node)
        add = []
        for kid in friends[node]:
            if kid in cmpnt:
                add.append(kid)
                cmpnt.remove(kid)

        blocked = set()
        for block in blocks[node]:
            blocked.add(block)
            
        ans[node] = len(cmpnt)-len(cmpnt&blocked)
        cmpnt.add(node)
        for kid in add:
            cmpnt.add(kid)

def main():
    n,m,k = map(int,input().split())
    friends = {}
    blocks = {}

    for i in range(1,n+1):
        friends[i] = []

    for i in range(1,n+1):
        blocks[i] = []

    for i in range(m):
        a,b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)

    for i in range(k):
        a,b = map(int,input().split())
        blocks[a].append(b)
        blocks[b].append(a)

    connected_compnts = []

    visited = set()
    for i in range(1,n+1):
        if i not in visited:
            dfs(i,visited,friends,connected_compnts)

    ans = [0]*(n+1)
    for cmpnt in connected_compnts:
        solve(cmpnt,friends,blocks,ans)

    for i in range(1,n+1):
        print(ans[i],end = ' ')

main()

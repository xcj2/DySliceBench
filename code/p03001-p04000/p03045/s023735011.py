import sys
sys.setrecursionlimit(150000)
def search(i, visited, ns) :
    #print(":", i+1)
    visited[i] = True
    for next, weight in ns[i]:
        if visited[next] == False:
            search(next, visited, ns)


def dfs(ns):
    visited = [False] * len(ns)
    ans = 0
    for i in range(len(ns)):
        if not visited[i]:
            #print(i+1)
            ans += 1
            search(i, visited, ns)
    return ans

def main():
    n,m = map(int,input().split())
    ns = [[] for _ in range(n)]
    for _ in range(m):
        (st,end,weight) = map(int,input().split())
        ns[st-1].append((end - 1,weight))
        ns[end-1].append((st-1,weight))
    ans = dfs(ns)
    print(ans)
if __name__ == '__main__':
    main()

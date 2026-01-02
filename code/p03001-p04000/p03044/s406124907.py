import sys
sys.setrecursionlimit(100000)
def search(i, visited, ns, ans) :
    #print(i+1)
    visited[i] = True
    for next, weight in ns[i]:
        if visited[next] == False:
            if weight % 2 == 0:
                ans[next] = ans[i]
            else:
                ans[next] = (ans[i]+1) % 2
            search(next, visited, ns, ans)


def dfs(ns, ans):
    visited = [False] * len(ns)
    search(0, visited, ns, ans)

def main():
    n = int(input())
    ns = [[] for _ in range(n)]
    for _ in range(n-1):
        (st,end,weight) = map(int,input().split())
        ns[st-1].append((end - 1,weight))
        ns[end-1].append((st-1,weight))
    ans = [False] * n
    dfs(ns, ans)
    for a in ans:
        if a:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()

from collections import deque
import sys
sys.setrecursionlimit(10**9)


def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()

def main():
    N = ii()

    u = 0
    graph = [[] for _ in range(10**5+10)]
    for i in range(N-1):
        u,v,w=mi()
        graph[u].append((v,w))
        graph[v].append((u,w))

    seen = set()
    stack = deque([u])

    ans=[[] for _ in range(N+1)]
    ans[u] = 0
    while stack:
        current = stack.popleft()

        for next, w in graph[current]:
            if next in seen: continue
            if w%2==0:
                ans[next] = ans[current]
            else:
                ans[next] = 0 if ans[current] == 1 else 1

            seen.add(next)
            stack.append(next)



    print(*ans[1:],sep='\n')




if __name__ == "__main__":
  main()

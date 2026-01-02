from collections import deque
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,M=mi()
    G = [[] for _ in range(N)]
    E = []
    for i in range(M):
        a,b = mi()
        a-=1; b -= 1 # 0-index

        G[a].append(b)
        G[b].append(a)
        E.append((a,b))
    
    deg1_v = -1
    for i in range(N):
        deg = len(G[i])
        if deg == 1:
            deg1_v = i
            break
    
    if deg1_v == -1:
        print(0)
        exit()

    ans = 0
    for i in range(M):
        a,b = E[i]
        G[a].remove(b)
        G[b].remove(a)

        visited_count = 0
        stack = deque([deg1_v])
        seen = set()
        visited = set()
        while stack:
            visited_count += 1
            current_e = stack.popleft()

            visited.add(current_e)
            for next in G[current_e]:
                if (current_e,next) in seen: continue
                stack.append(next)
                seen.add((current_e,next))
    
        if len(visited) != N:
            # print(a+1,b+1)
            ans += 1
    
        G[a].append(b)
        G[b].append(a)
    
    print(ans)





    


if __name__ == "__main__":
    main()
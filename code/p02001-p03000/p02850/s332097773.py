from collections import deque
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    G = [[] for _ in range(N)]
    E = []
    _E = set()
    for i in range(N-1):
        a,b=mi()
        G[a-1].append(b-1)
        G[b-1].append(a-1)
        E.append((a-1,b-1))
        _E.add((a-1,b-1))
    
    leaf = 0
    for i in range(N):
        g = G[i]
        if len(g) == 1:
            leaf = i

    stack = deque([(leaf,1,None)])
    seen = set()
    path = {x:0 for x in E}
    K = 0

    def save(edge,color):
        if edge == None: return

        a,b = edge
        if (a,b) in _E:
            path[(a,b)] = color
        else:
            path[(b,a)] = color


    while stack:
        current,color,edge = stack.popleft()
        seen.add(current)
        save(edge,color)
        K = max(K,color)
        # print(current,color,edge)

        i = 1
        for next in G[current]:
            if next in seen: continue
            if color == i:
                i += 1
            
            stack.append((next,i,(current,next)))
            i += 1
    
    if N == 2:
        print(1)
        print(1)
        exit()


    print(K)
    for i in range(N-1):
        a,b = E[i]
        print(path[(a,b)],sep="")







if __name__ == "__main__":
    main()
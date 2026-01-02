import sys
import collections

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, m = MI()
    G = [set() for _ in range(n+1)]
    for _ in range(m):
        a, b =MI()
        G[a].add(b)
        G[b].add(a)
    for i in range(n+1):
        G[i] = list(G[i])
    num = [-1]*(n+1)
    seen = [False]*(n+1)
    stack = []
    for i in range(1, n+1):
        if not seen[i]:
            stack.append(i)
            while stack:
                vertex = stack.pop(-1)
                seen[vertex] = True
                num[vertex] = i
            
                for j in range(len(G[vertex])):
                    neighbor = G[vertex][j]
                    if not seen[neighbor]:
                        stack.append(neighbor)
    c = collections.Counter(num)
    print(c.most_common()[0][1])

if __name__ == '__main__':
    main()
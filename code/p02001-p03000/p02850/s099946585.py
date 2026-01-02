import sys
from collections import deque, defaultdict
def input() : return sys.stdin.readline().strip()

def main():
    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N-1)]
    to = [[] for i in range(N)]

    for edge in edges:
        a, b = edge
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)
    
    colors = defaultdict(int)
    def bfs():
        q = deque() # (index, parent color)
        q.append((0, 0))
        while len(q):
            now, par_col = q.popleft()
            color = 0
            for v in to[now]:
                x, y = sorted([v, now])
                if colors[(x, y)]:
                    continue
                else:
                    color += 1
                    if color == par_col:
                        color += 1

                    colors[(x, y)] = color
                    q.append((v, color))
    bfs()

    ans = max(colors.values())
    print(ans)
    
    for edge in edges:
        x, y = edge
        x -= 1
        y -= 1
        print(colors[(x, y)])

                


        



if __name__ == "__main__":
    main()
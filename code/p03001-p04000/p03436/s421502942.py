import sys
from collections import deque
def input():return sys.stdin.readline().strip()

def main():
    H, W = map(int, input().split())
    
    field = "#" * (W+2)
    field += "#" + "##".join([input() for _ in range(H)]) + "#"
    field += "#" * (W+2)

    move = [-1, 1, -(W+2), W+2]
    cost = [0] * (H+2) * (W+2)

    def bfs(s):
        q = deque()
        enqueue = q.append
        dequeue = q.popleft
        cost[s] = 1
        enqueue(s)

        while q:
            now = dequeue()
            for dx in move:
                nv = now + dx
                if field[nv] != "#" and cost[nv] <= 0:
                    cost[nv] = cost[now] + 1
                    enqueue(nv)
        
    start = (W+2) + 1
    goal = H*(W+2) + W

    bfs(start)
    white = field.count(".")
    if cost[goal]:
        print(white - cost[goal])
    else:
        print(-1)
    
if __name__ == "__main__":
    main()
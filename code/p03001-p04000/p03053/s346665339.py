import sys
from collections import deque
def input():return sys.stdin.readline().strip()

def main():
    H, W = map(int, input().split())

    field = "#" * (W+2)
    field += "#" + "##".join([input() for _ in range(H)]) + "#"
    field += "#" * (W+2)

    move = [-1, 1, -(W+2), W+2]
    cost = [-1] * (H+2) * (W+2)

    def dfs(s):
        q = deque()
        enqueue = q.append
        dequeue = q.popleft

        for v in s:
            cost[v] = 0
            enqueue(v)

        while q:
            now = dequeue()
            cost_now = cost[now]
            for dx in move:
                nv = now + dx
                if field[nv] == "." and cost[nv] < 0:
                    cost[nv] = cost_now + 1
                    enqueue(nv)
    
    starts = [i*(W+2)+j for j in range(1, W+1) for i in range(1, H+1) if field[i*(W+2)+j] == "#"]
    dfs(starts)

    print(max(cost))

if __name__ == "__main__":
    main()
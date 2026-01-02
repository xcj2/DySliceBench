import sys
from collections import deque
input = sys.stdin.readline

class Node:
    def __init__(self, num):
        self.link = []
        self.costs = [num, num]
        self.check = False

def clear_nodes(nodes):
    for node in nodes:
        node.check = False

def main():
    N, u, v = map(int, input().split())

    nodes = [Node(N+1) for i in range(N+1)]

    for i in range(N-1):
        a, b = map(int, input().split())
        nodes[a].link.append(nodes[b])
        nodes[b].link.append(nodes[a])
    
    starts = [u, v]
    for i in range(2):
        clear_nodes(nodes)
        q = deque()
        q.append((nodes[starts[i]], 0))
        while len(q) > 0:
            node, cost = q.popleft()
            node.costs[i] = cost
            for next_node in node.link:
                if not next_node.check:
                    q.append((next_node, cost + 1))
                    next_node.check = True

    if nodes[u].costs[1] == 1:
        print(0)
        return

    clear_nodes(nodes)
    q = deque()
    ans = 0
    q.append(nodes[u])
    while len(q) > 0:
        node = q.popleft()
        ans = max(ans, node.costs[1])
        for next_node in node.link:
            if (not next_node.check) and next_node.costs[0] < next_node.costs[1]:
                q.append(next_node)
                next_node.check = True
    print(ans - 1)

    


if __name__ == "__main__":
    main()
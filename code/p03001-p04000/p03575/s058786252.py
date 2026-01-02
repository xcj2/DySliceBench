import sys

class Node:
    def __init__(self, node_num):
        self.node_num = node_num
        self.connect = []
    def add_node(self, node):
        self.connect.append(node)
    def delete_node(self, node):
        self.connect.remove(node)

def is_connect(node_list):
    check_list = [0]
    stack = [node_list[0]]
    while len(stack) != 0:
        if len(check_list) == N:
            return True
        current = stack.pop()
        for ii in current.connect:
            if ii not in check_list:
                check_list.append(ii)
                stack.append(node_list[ii])
    return (len(check_list) == N)
        
N, M = list(map(int, sys.stdin.readline().strip().split(" ")))
node_list = [Node(i) for i in range(N)]
edge_list = []

for i in range(M):
    n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
    node_list[n - 1].add_node(m - 1)
    node_list[m - 1].add_node(n - 1)
    edge_list.append((n-1, m-1))
    
res = 0
prev_edge = None
for e in edge_list:
    if prev_edge is not None:
        node_list[prev_edge[0]].add_node(prev_edge[1])
        node_list[prev_edge[1]].add_node(prev_edge[0])
    prev_edge = e
    node_list[e[0]].delete_node(e[1])
    node_list[e[1]].delete_node(e[0])
    if not is_connect(node_list):
        res += 1

print(str(res))

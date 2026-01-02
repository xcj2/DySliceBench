from collections import deque
N, Q = [int(item) for item in input().split()]

tree_list = [input().split() for j in range(1, N)]
query_list = [input().split() for k in range(Q)]


class Node:
    def __init__(self, val):
        self.val = val
        self.child_list = []
        self.cnt = 0

class my_tree:
    def __init__(self, tree_list):
        self.node_list = []

        for i in range(N):
            self.node_list.append(Node(i+1))

        for a, b in tree_list:
            a, b = int(a), int(b)

            child_node = self.node_list[b-1]
            parent_node = self.node_list[a-1]
            self.node_list[a-1].child_list.append(child_node)
            self.node_list[b-1].child_list.append(parent_node)
        
    def adding(self, query_list):
        for a, data in query_list:
            a, data = int(a), int(data)
            self.node_list[a-1].cnt += data

        stack = deque([self.node_list[0]])
        parent_node_list = [self.node_list[0]]*(N + 1)

        while True:
            v = stack.pop()
            for child in v.child_list:
                if child != parent_node_list[v.val -1]:
                    child.cnt += v.cnt
                    parent_node_list[child.val -1] = v
                    stack.append(child)
            
            if not stack:
                break


ins = my_tree(tree_list)
ins.adding(query_list)
print(*[node.cnt for node in ins.node_list])

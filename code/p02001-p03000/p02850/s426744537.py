from collections import deque
import sys
input = sys.stdin.readline

class Node:
    nodes = {}
    max_c = 0
    @classmethod
    def get_root_node(cls):
        n = Node.nodes[1]
        for _ in range(1000000):
            if n.parent is None:
                return n
            else:
                n = n.parent

    @classmethod
    def dump_all_nodes(cls):
        for key, node in Node.nodes.items():
            print(str(node))

    @classmethod
    def get_instance(cls, id, parent):
        if id in Node.nodes:
            if Node.nodes[id].parent is None:
                Node.nodes[id].parent = parent
            return Node.nodes[id]
        else:
            return Node(id, parent)

    @classmethod
    def color_childs(clf, start_node):
        c = 1
        list_to_visit = deque(start_node.childs)
        list_to_visit.append(-1)
        ap = list_to_visit.append

        while(len(list_to_visit)>0):
            if list_to_visit[0]==-1:
                c = 1
                list_to_visit.popleft()
                continue
            node = list_to_visit[0]
            list_to_visit.popleft()
            if c == node.parent.parent_edge_color:
                c += 1
            node.parent_edge_color = c
            if c > Node.max_c:
                Node.max_c = c
            list_to_visit += deque(node.childs)
            ap(-1)
            c += 1

    def __init__(self, id, parent):
        self.id = id
        self.parent = parent # None if root Node
        self.parent_edge_color = None
        self.childs = []
        Node.nodes[id] = self
        self.used_color = []

    def __str__(self):
        x = self.parent.id if self.parent else "None"
        #return f"id: {self.id}, parent: {x}, parent_edge_color: {self.parent_edge_color} ,num_child {len(self.childs)}, num_color {self.num_color}"
        return str(self.id)

    def append_child(self, node):
        self.childs.append(node)

    @property
    def num_color(self):
        if self.parent_edge_color is None:
            return len(self.childs)
        else:
            return len(self.childs) + 1

N = int(input())

Edges = []
Edges_color = []
ap = Edges.append
for i in range(N-1):
    edge = list(map(int, input().split()))
    ap(edge)
    pnode = Node.get_instance(edge[0], None)
    cnode = Node.get_instance(edge[1], pnode)
    pnode.append_child(cnode)

root = Node.get_root_node()

Node.color_childs(root)
#Node.dump_all_nodes()
K = Node.max_c
print(K)

for edge in Edges:
    print(Node.get_instance(edge[1], edge[0]).parent_edge_color)
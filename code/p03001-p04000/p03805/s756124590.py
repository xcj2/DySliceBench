# -*- coding: utf-8 -*-
# 13:50 -> 

class Node():
    def __init__(self, idx):
        self.idx = idx
        self.next_node = []
    
    def add_node(self, node):
        self.next_node.append(node)

N, M = map(int, input().split())
nodes = {i:Node(i) for i in range(1,N+1)}

for m in range(M):
    a,b = map(int, input().split())
    nodes[a].add_node(nodes[b])
    nodes[b].add_node(nodes[a])

def permutation_search(idxs, now_idx):
    if len(idxs) == 0:
        return 1

    num = 0
    for i in range(len(idxs)):
        next_idx = idxs[i]
        next_idxs = idxs[:i]+idxs[i+1:]
        if next_idx in [node.idx for node in nodes[now_idx].next_node]:
            num += permutation_search(next_idxs, next_idx)
    
    return num

total = permutation_search([i for i in range(2,N+1)], 1)

print(total)
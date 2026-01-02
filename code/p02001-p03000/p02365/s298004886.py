# Acceptance of input

import sys

file_input = sys.stdin

v_num, e_num, r = map(int, file_input.readline().split())

G = [[] for i in range(v_num)]

import heapq

for line in file_input:
    s, t, w = map(int, line.split())
    if t != r:
        heapq.heappush(G[t], [w, s, t])

# Edmonds' algorithm

def find_cycle(incoming_edges, root):
    in_tree = [False] * v_num
    in_tree[root] = True
    for e in incoming_edges:
        if e:
            S = []
            S.append(e[2])
            while True:
                p = incoming_edges[S[-1]][1]
                if in_tree[p]:
                    while S:
                        in_tree[S.pop()] = True
                    break
                elif p in S:
                    return S[S.index(p):] # return nodes in a cycle
                else:
                    S.append(p)
    return None

def contract_cycle(digraph, cycle_node, root):
    super_node = cycle_node[0]
    for edges in digraph:
        if edges:
            min_weight = edges[0][0]
            for e in edges:
                e[0] -= min_weight
                if e[1] in cycle_node:
                    e[1] = super_node
                if e[2] in cycle_node:
                    e[2] = super_node
    contracted_edges = []
    for n in cycle_node: 
        for e in digraph[n]:
            if e[1] != super_node:
                heapq.heappush(contracted_edges, e)
        digraph[n].clear()
    digraph[super_node] = contracted_edges

def edmonds_branching(digraph, root, weight):
    min_incoming_edges = [None] * v_num
    for edges in digraph:
        if edges:
            min_edge = edges[0]
            min_incoming_edges[min_edge[2]] = min_edge
            weight += min_edge[0]
    C = find_cycle(min_incoming_edges, root)
    if not C:
        return weight
    else:
        contract_cycle(digraph, C, r)
        return edmonds_branching(digraph, root, weight)

# output
print(edmonds_branching(G, r, 0))
import heapq
from typing import List, Optional


def _find_cycle(incoming_edges: List[List[int]], root: int) -> Optional[List[int]]:
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
                    return S[S.index(p):]
                else:
                    S.append(p)
    return None


def _contract_cycle(digraph: List[List[List[int]]],
                    cycle_node: List[int], root: int) -> None:
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
    contracted_edges: List[List[int]] = []
    for n in cycle_node:
        for e in digraph[n]:
            if e[1] != super_node:
                heapq.heappush(contracted_edges, e)
        digraph[n].clear()
    digraph[super_node] = contracted_edges


def edmonds_branching(digraph: List[List[List[int]]], root: int, weight: int) -> int:
    min_incoming_edges: List[List[int]] = [[]] * v_num
    for edges in digraph:
        if edges:
            min_edge = edges[0]
            min_incoming_edges[min_edge[2]] = min_edge
            weight += min_edge[0]
    C = _find_cycle(min_incoming_edges, root)
    if not C:
        return weight
    else:
        _contract_cycle(digraph, C, r)
        return edmonds_branching(digraph, root, weight)


if __name__ == "__main__":
    v_num, e_num, r = map(lambda x: int(x), input().split())
    G: List[List[List[int]]] = [[] for i in range(v_num)]

    for _ in range(e_num):
        s, t, w = map(lambda x: int(x), input().split())
        if t != r:
            heapq.heappush(G[t], [w, s, t])

    print(edmonds_branching(G, r, 0))


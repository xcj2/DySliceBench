import sys
input=sys.stdin.readline
import math

def get_edges_include_node(i, Edges): # 頂点 i を含む辺のリストを返す
    es = []
    for e in Edges:
        if i in e:
            es.append(e)
    return es

def dfs(i, e0, goal, Edges): # 頂点 i から頂点 j にたどり着けるかどうか
    if e0 in Edges:
        Edges.remove(e0)
    for e1 in get_edges_include_node(i, Edges):
        if goal in e1:
            return True
        else:
            ni = e1[1] if e1[0] == i else e1[0]
            if dfs(ni, e1, goal, Edges):
                return True                
    return False
def main():

    N,M = map(int, input().split())
    Edges = []
    for _ in range(M):
        a,b = map(int, input().split())
        Edges.append((a,b))
    ans = 0
    for e in Edges:
        tmp = []
        for e2 in Edges:
            tmp.append((e2[0], e2[1]))
        if not dfs(e[0], e, e[1], tmp):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()

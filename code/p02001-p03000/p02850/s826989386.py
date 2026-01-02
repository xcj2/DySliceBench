#!/usr/bin/env python3
 
import sys
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()


def main():
    input = sys.stdin.readline      # 改行文字が残ることに注意
    def ii():  return int(input())
            

    def bfs_tree_traverse(root):
        ' root から BFS し条件を満たすように彩色していく。各辺の色情報を color に記載。最後に使用した色の数を返す。'
        paths = deque([root])
        max_branch = 0
        while len(paths) != 0:
            edge_color = 0
            current = paths.popleft()
            parent_edge_color = color[current]
            for v in adj[current]:
                paths.append(v)
                edge_color += 1
                if edge_color == parent_edge_color:
                    edge_color += 1
                color[v] = edge_color
                max_branch = max(max_branch, edge_color)
        return max_branch
        
 
    n = ii()
    # 各辺の両端の頂点 index を保存したペア (tuple) の list
    L = [tuple(map(lambda x: int(x)-1, input().rstrip().split())) for _ in range(n-1)]
    # 隣接リスト 親->子のみリンクをはれば十分
    adj = [[] for _ in range(n)]
    for pair in L:
        a, b = pair
        adj[a].append(b)
    # 各辺の子供の index と色情報 (int) の対応記載される隣接行列 
    color = [0] * n
    
    print(bfs_tree_traverse(0))
    for pair in L:
        _, b = pair
        print(color[b])
 
if __name__ == "__main__":
    main()
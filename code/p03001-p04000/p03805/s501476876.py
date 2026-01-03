def examC():
    def search_graph(graph_releation, result_list, current_idx=0, path=[0]):
        for i in range(len(graph_releation[current_idx])):
            next_idx = graph_releation[current_idx][i]
            #次の点の候補全部ひとつずつやる
            tmp_path = copy.deepcopy(path)
            #今まで通った点
            if next_idx in tmp_path:
                #通ったことがある
                continue
            tmp_path.append(next_idx)
            if len(tmp_path) == len(graph_releation):
                #今まで通った点が点全部になった
                result_list.append(tmp_path)  # 確定
                continue
            else:
                search_graph(graph_releation, result_list, next_idx, tmp_path)
                #次の点から出る辺でチェック

    N, M = LI()
    v = [[] for _ in range(N)]
    for i in range(M):
        a, b = LI()
        v[a-1].append(b-1)
        v[b-1].append(a-1)
    cur = []
    search_graph(v, cur)
    print(len(cur))
#    print(cur)

import sys
import copy
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()

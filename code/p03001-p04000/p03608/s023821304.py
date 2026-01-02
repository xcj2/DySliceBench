from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    # 負の閉路を持つ場合は'NEGATIVE CYCLE'を、そうでない場合には(i,j)成分に
    # 頂点iから頂点jへの最短経路の距離を格納するdist_listをprintする関数
    def warshall_floyd(v_num, dist_lst):
        # 負の閉路を持つか
        negative_cycle_flag = False
    
        # 頂点iから頂点jへの経路と、頂点kを経由した場合の経路とを比較して
        # よりコストの合計が小さい方を配列に入れる動的計画法
        for k in range(v_num):
            for i in range(v_num):
                for j in range(v_num):
                    # i→k→jがつながっててしかもi→jルートよりもイケてるなら更新
                    if dist_lst[i][k] != INF and dist_lst[k][j] != INF:
                        if dist_lst[i][j] > dist_lst[i][k] + dist_lst[k][j]:
                            dist_lst[i][j] = dist_lst[i][k] + dist_lst[k][j]
    
        for v in range(v_num):
            # dist_lstに負の数が格納されているとは、
            # グラフが負の閉路を持つことを意味する
            if dist_lst[v][v] < 0:
                negative_cycle_flag = True
    
        return dist_lst
    
    
    # 頂点の数と辺の数

    v_num, e_num ,R= map(int, input().split())
    r=list(map(int,input().split()))
    
    # 配列dist_lst[a][b]には頂点a,b間の辺のコストを入れておき、
    # a=bの時は0を、a,b間の辺が存在しないときはINFを入れておく。
    INF = 10 ** 20
    dist_lst = [[INF] * v_num for _ in range(v_num)]
    
    for _ in range(e_num):
        s, t, dist = map(int, input().split())
        dist_lst[s-1][t-1] = dist
        dist_lst[t-1][s-1] = dist

    
    for v in range(v_num):
        dist_lst[v][v] = 0
    
    ll=warshall_floyd(v_num, dist_lst)
    minans=10**10
    for i in permutations(r):
        ans=0
        for j in range(len(i)-1):
            if ll[i[j]-1][i[j+1]-1]==INF or ll[i[j]-1][i[j+1]-1]==0:
                break
            else:
                ans+=ll[i[j]-1][i[j+1]-1]
        minans=min(minans,ans)
    print(minans)


    
      
    
resolve()
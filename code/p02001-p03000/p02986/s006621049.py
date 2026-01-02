
class Accumulate:
    def __init__(self,lst): #g: graph 
        from itertools import accumulate
        self.acc = list(accumulate([0]+lst))

    def query(self,u,v): #[u,v]の和を返す（閉区間）
        return self.acc[v+1] - self.acc[u]



"""
オイラーツアー（辺属性）　http://beet-aizu.hatenablog.com/entry/2019/07/08/174727
部分木に関するクエリを処理

ds[v] = v は行きがけで ls[v]番目の頂点
us[v] = v の帰りがけ時、すでに行きがけに確認した頂点の個数

v の部分木に属する頂点は [ls[v],rs[v]) までの頂点
"""

class Euler_tour_edge:
    """
    parent: ダブリングテーブル
    depth: 元の深さ
    """
    def __init__(self,g,root): #g: graph 

        def dfs(root):
            n = len(g)
            parent = self.parent[0]
            q = [root]
            cnt = 0
            q_wt = [0]; q_col = [0] #辺の情報をためるスタック
            data_wt = []; data_col = [] #辺の情報を順番に保持したデータ
            while q:
                v = q.pop()
                if v >= 0: #行きがけ
                    q.append(-v-1)
                    self.ds[v] = cnt; cnt += 1
                    if v != root: #辺の情報（行きがけ）
                        data_wt.append(q_wt[-1]); data_col.append(q_col[-1]);
                    for c,col,wt in g[v]:
                        if c != parent[v]:
                            parent[c] = v
                            self.depth[c] = self.depth[v] + 1
                            q.append(c);
                            q_wt.append(wt); q_col.append(col) #辺の情報
                else: #帰りがけ
                    #辺の情報（帰りがけは辺のコストを -1 倍）
                    data_wt.append(-q_wt.pop()); data_col.append(q_col.pop())
                    self.us[-v-1] = cnt; cnt += 1
            data_wt.pop(); data_col.pop() #最後のデータはダミー
            #print(data_wt,data_col)
            #print(self.us,self.ds)
            return data_wt, data_col        
            
        def doubling_make_table(N,logN,Table):
            for i in range(1,logN):
                for j, Tiij in enumerate(Table[i-1]):
                    if Tiij != -1:
                        Table[i][j] = Table[i-1][Tiij]

        N = len(g)
        self.logN = len(bin(N))-2
        self.parent = [[-1]*N for _ in range(self.logN)]
        self.depth = [0]*(N) #ノードの深さ
        self.ds = [0]*(n)
        self.us = [0]*(n)
        data_wt,data_col = dfs(root)
        doubling_make_table(N, self.logN, self.parent) #ダブリングのテープル構築

        #以下、data を用いてデータ構造を構成
        #print(data)
        self.wt_acc = Accumulate(data_wt)
        self.color_id = [[] for _ in range(n)]
        self.color_num = [[0] for _ in range(n)]
        self.color_acc = [[0] for _ in range(n)]
        for i,(c,w) in enumerate(zip(data_col,data_wt)):
            self.color_id[c].append(i)
            self.color_num[c].append(self.color_num[c][-1] + (1 if w>0 else -1))
            self.color_acc[c].append(self.color_acc[c][-1]+w)
        
        #print(self.wt_acc.acc)
        #print(self.ds,self.us)
    
            
    def get_path_wt(self,col,wt,u,v):
        p = self.getLCA(u,v)
        #print("p",p,self.ds[p],"u",u,self.ds[u],"v",v,self.ds[v])
        res = self.wt_acc.query(self.ds[p],self.ds[u]-1) + self.wt_acc.query(self.ds[p],self.ds[v]-1)
        # res = u-v 間のパスの重みが求まった
        cid  = self.color_id[col] 
        cnum = self.color_num[col]
        cacc = self.color_acc[col]
        if cid:
            i = bisect_left(cid,self.ds[u])
            res += (-cacc[i] + wt*cnum[i])
            i = bisect_left(cid,self.ds[v])
            res += (-cacc[i] + wt*cnum[i])
            i = bisect_left(cid,self.ds[p])
            res -= 2*(-cacc[i] + wt*cnum[i])
        return res
        

    def getLCA(self,u,v): #u,vのLCAを返す
        if self.depth[u] > self.depth[v]: u,v = v,u #vが深い
        dd = self.depth[v] - self.depth[u]
        for k in range(self.logN-1,-1,-1):
            if (dd >> k) & 1: v = self.parent[k][v]
        if u == v: return u;
        for k in range(self.logN-1,-1,-1):
            if self.parent[k][u] != self.parent[k][v]:
                u,v = self.parent[k][u], self.parent[k][v]
        return self.parent[0][u];

    def getdepth(self,u): #uの深さを返す
        return self.depth[u]



#####################################

# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline 
readlines = sys.stdin.readlines

#n = int(input())
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

n,m = [int(i) for i in readline().split()]
abcd = map(int,read().split())

g = [[] for _ in range(n)]

for i in range(n-1):
    a,b,c,d = next(abcd),next(abcd),next(abcd),next(abcd)
    a -= 1; b -= 1
    #print(a,b,c,d)
    g[a].append([b,c,d])
    g[b].append([a,c,d])


#print(g)
E = Euler_tour_edge(g,0)

ans = [0]*m

from bisect import bisect_left

for i in range(m):
    c,w,u,v = next(abcd),next(abcd),next(abcd),next(abcd)
    u -= 1; v -= 1
    #print(E.get_path_wt(c,w,u,v))
    ans[i] = E.get_path_wt(c,w,u,v)

print("\n".join(map(str,ans)))




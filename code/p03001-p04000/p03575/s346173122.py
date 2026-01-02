class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def Union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # これ抜かさないで！！！！
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def same(self,x,y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False
#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from itertools import combinations # (string,3) 3回
#from collections import deque
#import collections.defaultdict
#import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n,m = readInts()
    #Uni = UnionFind(n)
    # 最初に保存しておく
    bridge = []
    for i in range(m):
        s,e = map(lambda x: int(x) - 1,input().split())
        bridge.append((s,e))
    cnt = 0
    for i in range(m):
        # ある辺を取り除いた時
        Uni = UnionFind(n)
        for j,root in enumerate(bridge,start = 0):
            # もし、取り除いた辺とidxが一緒ならば、次にいく
            if i == j:
                continue
            s,t = root
            Uni.Union(s,t)
        # ここで構成完了
        s,t = bridge[i]
        if not Uni.same(s,t): # 頂点が一致しない # その経路は必要だった
            cnt += 1
    print(cnt)


if __name__ == '__main__':
  main()

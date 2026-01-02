import sys, math
from collections import defaultdict
from itertools import product
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

class Graph:
    #グラフを表す

    # 頂点につけるlabelの初期値（ラベリングされていないことを示す値）
    no_labeling_num = -1

    class Vertex:
        # 頂点を表す

        def __init__(self, g, no, label):
            """

            :param g: グラフを表す。またVertexを所有するオブジェクトでもある
            :param no: 頂点にグラフのなかで一意に割り振られた識別用の番号
            :param label: 探索された順番を表す番号。ラベル。
            """
            self.no = no
            self.g = g
            self.label = label

        def __str__(self):
            """
            　
            """
            return "no:{0},label:{1}".format(self.no,self.label)

        def adjacentVs(self):
            """ selfと隣接している頂点のリストを返す

            :return:
            """
            result = []
            for c in range(self.g.order):
                if self.g.aDJM[self.no][c] == 1:
                    result.append((self.g.vs[c]))
            return result

        def back_to_previous(self):
            """ 前に探索した頂点を返す（厳密な表現ではない）
            詳細
            ・この頂点に隣接する頂点において、ラベル付けされていない（未探索）なものがないときに、
            次に探索する頂点を返す関数
            ・自身のラベル番号より小さい頂点の中で一番近いものを返す
            ・存在しないときは「None」を返す

            :return:
            """
            result = None
            vs = list(filter(lambda x: self.label > x.label, self.adjacentVs()))
            if vs != []:
                result = vs[0]
                key0 = self.label - result.label
                for v in vs:
                    key1 = self.label - v.label
                    if (key1 < key0):
                        key0 = key1
                        result = v

            return result

    def __init__(self, aDJM):
        """
        
        :param aDJM:隣接行列
        """
        self.aDJM = aDJM
        self.order = len(aDJM)
        self.vs = [Graph.Vertex(self, i, self.no_labeling_num) for i in range(self.order)]

    def no_labelingVs(self, vs):
        """ 渡された頂点リストにおいてlabelingされていない頂点のリストを返す

        :return:
        """
        result = []
        for v in vs:
            if v.label == self.no_labeling_num:
                result.append(v)
        return result

    def isconnected(self):
        """ このグラフが連結グラフであるかどうかを判定する
        
        :return:
        """
        label = 0
        v = self.vs[0]
        v.label = label
        # 最初に探索した頂点が孤立点である場合に対処するための条件
        if v.adjacentVs()==[]:
            v=None
        else:
            v = v.adjacentVs()[0]
            label += 1
            v.label = label
        while (v != None):  # 現在探索中の頂点のラベルが0かつその点に隣接する頂点すべてが探索ずみだったら終了するようにする
            vs = self.no_labelingVs(v.adjacentVs())
            if vs == []:
                v = v.back_to_previous()
            else:
                v = vs[0]
                label += 1
                v.label = label

        return not(self.no_labeling_num in list(map(lambda x:x.label,self.vs)))


def main():
    N, M = mi()
    aDJM = [[0]*N for i in range(N)]
    a, b = i2(M)
    cnt = 0

    for i in range(M):
        aDJM[a[i]-1][b[i]-1] = 1
        aDJM[b[i]-1][a[i]-1] = 1
    
    for i in range(M):
        aDJM[a[i]-1][b[i]-1] = 0
        aDJM[b[i]-1][a[i]-1] = 0
        if not Graph(aDJM).isconnected():
            cnt += 1
        aDJM[a[i]-1][b[i]-1] = 1
        aDJM[b[i]-1][a[i]-1] = 1

    print(cnt)

if __name__ == '__main__':
    main()
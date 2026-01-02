class BinaryIndexedTree:
    def __init__(self, size=10**7):
        self.size = size
        self.data = [0]*(size+1)

    def add(self, index, x):
        while index <= self.size:
            self.data[index] += x
            index += index & -index

    def prefix_sum(self, index):
        res = 0
        while index >= 1:
            res += self.data[index]
            index -= index & -index
        return res
    
    def interval_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left-1)

    def __getitem__(self, index):
        return self.sum(index) - self.sum(index-1)

    # def __setitem__(self, index, x):
    #     before = self.__getitem__(index)
    #     self.add(index, -before)
    #     self.add(index, x)

def main():
    from sys import stdin
    input = lambda: stdin.readline()
    LMIIS = lambda: list(map(int,input().split()))


    N,Q = LMIIS()
    # 1-indexedにするためリストの先頭に0を追加
    C = [0] + LMIIS()
    queries = []

    # 順番と一緒にクエリを保存
    for i in range(Q):
        l,r = map(int,input().split())
        queries.append((i,l,r))
    
    # rについてクエリをソート
    queries.sort(key=lambda x: x[2])

    # 玉の種類 -> 良い玉の場所
    good_ball_places = [0] * (N+1)

    # 場所 -> 良い玉が存在するなら1,しないなら0
    good_ball_exists = BinaryIndexedTree(N)

    #　玉の更新済み範囲
    k = 0
    # クエリの回答
    out = [0] * Q
    for order,l,r in queries:
        for i in range(k+1,r+1):
            # 位置iの玉の色
            color = C[i]
            # 色colorの良い玉の前の位置
            before = good_ball_places[color]
            # 色colorが既出なら、前の位置での存在を消去
            if 0 < before:
                good_ball_exists.add(before,-1)
            # 色colorの良い玉の位置はi
            good_ball_places[color] = i
            # 位置iに良い玉が存在
            good_ball_exists.add(i,1)
        # 良い玉を更新した範囲
        k = r
        # [l,r]に存在する良い玉の数の合計
        out[order] = good_ball_exists.interval_sum(l,r)
    print('\n'.join(map(str,out)))


        








    
main()
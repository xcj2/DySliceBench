import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    """
    とりあえず，S,TはXだけ左にずらして，0秒の時にどの時間ならXで止まるかにする．
    そのあと，グラフ(x-tグラフ)を書いて，縦棒を左から動かしていく（イベントソート）
    通行止めとなるXを複数持っておく必要があり，追加，参照，削除の機能が欲しい
    """

    ##############################
    from bisect import bisect_left, bisect_right, insort_right
    class SquareSkipList:
        # SkipList の層数を 2 にした感じの何か
        # std::multiset の代用になる

        def __init__(self, values=None, sorted_=False, square=1000, seed=42):
            # values: 初期値のリスト
            # sorted_: 初期値がソート済みであるか
            # square: 最大データ数の平方根
            # seed: 乱数のシード
            ### pop関数は　for を回すので重め、使うなら square パラメータを大きめにするべき

            self.cnt=0#要素数を持っておくか
            inf = float("inf")
            self.square = square
            if values is None:
                self.rand_y = seed
                self.layer1 = [inf]
                self.layer0 = [[]]
            else:
                self.layer1 = layer1 = []
                self.layer0 = layer0 = []
                if not sorted_:
                    values.sort()
                y = seed
                l0 = []
                for v in values:
                    y ^= (y & 0x7ffff) << 13
                    y ^= y >> 17
                    y ^= (y & 0x7ffffff) << 5
                    if y % square == 0:
                        layer0.append(l0)
                        l0 = []
                        layer1.append(v)
                    else:
                        l0.append(v)
                layer1.append(inf)
                layer0.append(l0)
                self.rand_y = y

        def add(self, x):  # 要素の追加  # O(sqrt(n))
            # xorshift
            y = self.rand_y
            y ^= (y & 0x7ffff) << 13
            y ^= y >> 17
            y ^= (y & 0x7ffffff) << 5
            self.rand_y = y

            if y % self.square == 0:
                layer1, layer0 = self.layer1, self.layer0
                idx1 = bisect_right(layer1, x)
                layer1.insert(idx1, x)
                layer0_idx1 = layer0[idx1]
                idx0 = bisect_right(layer0_idx1, x)
                layer0.insert(idx1+1, layer0_idx1[idx0:])  # layer0 は dict で管理した方が良いかもしれない  # dict 微妙だった
                del layer0_idx1[idx0:]
            else:
                idx1 = bisect_right(self.layer1, x)
                insort_right(self.layer0[idx1], x)

            self.cnt+=1#追加

        def remove(self, x):  # 要素の削除  # O(sqrt(n))
            # x が存在しない場合、x 以上の最小の要素が削除される
            idx1 = bisect_left(self.layer1, x)
            layer0_idx1 = self.layer0[idx1]
            idx0 = bisect_left(layer0_idx1, x)
            if idx0 == len(layer0_idx1):
                del self.layer1[idx1]
                self.layer0[idx1] += self.layer0.pop(idx1+1)
            else:
                del layer0_idx1[idx0]

            self.cnt-=1

        def search_higher_equal(self, x):  # x 以上の最小の値を返す  O(log(n))
            idx1 = bisect_left(self.layer1, x)
            layer0_idx1 = self.layer0[idx1]
            idx0 = bisect_left(layer0_idx1, x)
            if idx0 == len(layer0_idx1):
                return self.layer1[idx1]
            return layer0_idx1[idx0]

        def search_higher(self, x):  # x を超える最小の値を返す  O(log(n))
            idx1 = bisect_right(self.layer1, x)
            layer0_idx1 = self.layer0[idx1]
            idx0 = bisect_right(layer0_idx1, x)
            if idx0 == len(layer0_idx1):
                return self.layer1[idx1]
            return layer0_idx1[idx0]

        def search_lower(self, x):  # x 未満の最大の値を返す  O(log(n))
            #x未満のものがない場合，infが返るかも！！！  
            idx1 = bisect_left(self.layer1, x)
            layer0_idx1 = self.layer0[idx1]
            idx0 = bisect_left(layer0_idx1, x)
            if idx0 == 0:  # layer0_idx1 が空の場合とすべて x 以上の場合
                return self.layer1[idx1-1]
            return layer0_idx1[idx0-1]

        def pop(self, idx):
            # 小さい方から idx 番目の要素を削除してその要素を返す（0-indexed）
            # O(sqrt(n))
            # for を回すので重め、使うなら square パラメータを大きめにするべき
            self.cnt-=1
            layer0 = self.layer0
            s = -1
            for i, l0 in enumerate(layer0):
                s += len(l0) + 1
                if s >= idx:
                    break
            if s==idx:
                layer0[i] += layer0.pop(i+1)
                return self.layer1.pop(i)
            else:
                return layer0[i].pop(idx-s)


        def all(self):
            print(self.layer1)
            print(self.layer0)

        def len(self):
            return self.cnt

    ##############################


    N,Q=MI()
    L=[]#0なら追加，1なら削除，2ならクエリ，半開区間なので順番大事
    for _ in range(N):
        s,t,x=MI()
        s-=x
        t-=x
        L.append([s,0,x])
        L.append([t,1,x])
        
    #制約よりDは昇順
    for _ in range(Q):
        d=I()
        L.append([d,2,0])#3つに揃えておくか
        
    L.sort()
    anss=[]
    inf=10**10
    ssl = SquareSkipList(square=2000)
    ssl.add(inf)
    
    for t,q,x in L:
        if q==0:
            ssl.add(x)
        elif q==2:
            temp=ssl.search_higher_equal(-1)#最小値検索
            if temp==inf:
                ans=-1
            else:
                ans=temp
            anss.append(ans)
        else:
            ssl.remove(x)
            
    for i in range(Q):
        print(anss[i])
                
            
        
        
    
    
main()


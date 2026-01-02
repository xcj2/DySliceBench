import queue



"""
start : スタートの盤面を表す配列
# bf_search([8, 6, 7, 2, 5, 4, 3, 0, 1])
bf_search([1,2,3,4,5,0,7,8,6])
bf_search([1,3,0,4,2,5,7,8,6])
"""


def bf_search(start):
    # 隣接リスト
    adjacent = (
        # 0のコマから1or3へ移動できる
        (1, 3),  # 0
        # 1のコマから0or2or4へ移動できる
        (0, 2, 4),  # 1
        (1, 5),  # 2
        (0, 4, 6),  # 3
        (1, 3, 5, 7),  # 4
        (2, 4, 8),  # 5
        (3, 7),  # 6
        (4, 6, 8),  # 7
        (5, 7)  # 8
    )
    # 最終的に至りたい形
    GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # 初期値の時点でゴールだったら
    if start == GOAL:
        print(0)
        return
    

    q = queue.Queue()
    
    # キューにStateオブジェクトを追加する
    q.put(State(start, start.index(0), None))
    
    # table:同一局面があるかチェックするための辞書（ハッシュ）
    table = {}
    
    # 配列をタプル型に変換してそれをキーとする
    # Trueなら一度見たことがある状態
    table[tuple(start)] = True

    # ゴールにたどり着くまでループ
    # キューが空になってループが終了　-> goalにたどり着けなかった
    while not q.empty():
        # キューから局面を取り出してaに格納
        a = q.get()
        #print(a.board)
        # adjacent[a.space]: 動かせるコマの位置
        """
        完成形から考えて
        空白0のインデックスが7だったら隣接リストより4,6,8の方向へを動かすことができるので
        
        最初のループでxに4が入る
        """
        #print("a.apace="+str(a.space))
        for x in adjacent[a.space]:
            #print("x="+str(x))
            # 元の局面をコピー(State型でなく状態のみ「startと同じ」)
            b = a.board[:]

            b[a.space] = b[x]
            # 0: 空き場所を表す
            b[x] = 0
            key = tuple(b)
            # 同一局面がないかチェック　あればcontinueでループをスキップ
            if key in table: continue
            # 同一局面がなければ新しい局面を生成
            c = State(b, x, a)
            if b == GOAL:
                # print("answer")
                min = Min()
                min.print_answer(c)
                min.result()
                return
            # 局面を追加
            q.put(c)
            table[key] = True


class State:
    def __init__(self, board, space, prev):
        # 盤面を表す配列
        self.board = board
        # 空き場所の位置
        self.space = space
        # ひとつ前の局面（Stateオブジェクト）
        self.prev = prev

class Min:
    def __init__(self):
        self.min = 0
    def increment(self):
        self.min = self.min + 1
    def result(self):
        print(self.min - 1)

    # 手順の表示
    def print_answer(self,x):
        if x is not None:
            self.increment()
            self.print_answer(x.prev)
            # print(x.board)



def main():
    p = []  ##appendのために宣言が必要
    # 入力受付
    i = 0
    while i < 3:
        try:
            p.append(list(map(int, input().split())))
            i = i + 1
        except:
            break;
    # ↓この形に変形したい
    # start =[1,3,0,4,2,5,7,8,6]
    start = sum(p,[])

    bf_search(start)

    return








if __name__ == '__main__':
    main()

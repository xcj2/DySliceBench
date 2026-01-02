# バックトラック法
class EightQueens:
    def __init__(self,p):
        self.p = p
        # 前提 8*8の盤
        self.N = 8
        # 下準備
        # row[k] : k行目におけるクイーンの列番号
        self.row = [None] * 8
        # col[n] : n列目上にクイーンがなければFREE,あればNOT_FREE,それが8列分
        self.col = ['FREE'] * 8
        # 8 * 8 のマスに対角線を引いていくと15本引くことができる
        # dpos : 45度方向の対角線　dneg : 135度方向の対角線
        self.dpos = ['FREE'] * 15
        self.dneg = ['FREE'] * 15

        # 入力された位置にクイーンを置く
        i = 0
        while i < len(p):
            self.row[p[i][0]] = p[i][1]
            self.col[p[i][1]] = self.dpos[p[i][0] + p[i][1]] = self.dneg[p[i][0] - p[i][1] + self.N - 1] = 'NOT_FREE'
            i = i + 1


        # self.printBoard()

    """
    盤面の状態を表示
    """
    def printBoard(self):
        i = 0
        while i < self.N:
            j = 0
            while j < self.N:
                if j == self.row[i]:
                    print("Q", end="")
                # elif self.col[j] == 'NOT_FREE' or self.dpos[i+j] == 'NOT_FREE' or self.dneg[i-j + self.N-1] == 'NOT_FREE':
                    # print("N ", end="")
                else:
                    print(".", end="")
                    #print("F ", end="")
                j = j + 1
            print()
            i = i + 1
        return

    def putQueen(self,i):
        N = self.N

        # 初期化で置かれたクイーンだったらスキップ
        k = 0
        while k < len(self.p):
            if i == self.p[k][0]:
                i = i + 1
                k = 0
            k = k + 1


        # iが8(9行目)に到達したら終了
        if i == N:
            # print("解を発見")
            self.printBoard()
            return

        j = 0
        while j < N :
            # print(str(i)+", "+str(j))
            # self.printBoard()

            # 置こうとした位置がそれ以前の行のクイーンの領域だったら次の列へスキップ
            if self.col[j] == 'NOT_FREE' or self.dpos[i+j] == 'NOT_FREE' or self.dneg[i-j + N-1] == 'NOT_FREE':
                # print("置けません")
                j = j + 1
                continue

            # クイーンを(i,j)に置く
            self.row[i] = j

            # print()
            self.col[j] = self.dpos[i+j] = self.dneg[i-j+N-1] = 'NOT_FREE'
            # 次の行にクイーンを置くことを試みる（ダメだったら戻る）
            self.putQueen(i+1)
            # バックトラックキングのために(i,j)からクイーンを取り除く
            self.col[j] = self.dpos[i+j] = self.dneg[i-j+N-1] = 'FREE'
            j = j + 1
        return





def main():
    p = []  ##appendのために宣言が必要
    # 入力受付
    k = int(input())
    i = 0
    while i < k:
        try:
            p.append(list(map(int, input().split())))
            i = i + 1
        except:
            break;

    # 読み込み完了
    # pを行でソート
    p.sort()
    q = EightQueens(p)
    q.putQueen(0)
    return






if __name__ == '__main__':
    main()

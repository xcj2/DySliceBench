import sys
import copy

k = int(input())


class Chessboard:
    def __init__(self):
        self.row = [True] * 8
        self.col = [True] * 8
        self.dpos = [True] * 15
        self.dneg = [True] * 15
        return

    def put(self, r, c):
        # queen が r, c に配置されたときに攻撃されるマスの記録
        self.row[r] = False
        self.col[c] = False
        self.dpos[r + c] = False  # 左下が攻撃される
        self.dneg[r + 7 - c] = False  # 右下が攻撃される
        return

    def safe(self, r, c):
        # r, c が攻撃されていないか確認する　攻撃されていないときTrue を返す
        return self.row[r] and self.col[c] and self.dpos[r + c] and self.dneg[r + 7 - c]

    def is_row(self, r):
        return self.row[r]


board = Chessboard()
ans = [['.'] * 8 for _ in range(8)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().strip().split())
    board.put(r, c)
    ans[r][c] = 'Q'
final_ans = None


def search(r=0, board=board, ans=ans):
    global final_ans
    if r == 8:  # 最終行を終了し探索する行が存在しないときに終了する
        final_ans = ans
        return ans
    if not board.is_row(r):
        # すでに Q が配置されている行の探索はスキップする
        search(r=r+1, board=board, ans=ans)

    for c in range(8):
        board_temp = copy.deepcopy(board)
        ans_temp = copy.deepcopy(ans)
        if board_temp.safe(r, c):
            board_temp.put(r, c)
            ans_temp[r][c] = 'Q'
            search(r=r+1, board=board_temp, ans=ans_temp)
        else:
            continue


ans = search()
for r_ans in final_ans:
    print(''.join(r_ans))



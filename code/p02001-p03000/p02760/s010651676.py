import sys
input = sys.stdin.readline

class Bingo():
    def __init__(self, board):
        self.board = board
        self.length = 3
        self.check = [[False] * self.length for i in range(self.length)]
    
    def punch(self, num):
        for i in range(self.length):
            for j in range(self.length):
                if self.board[i][j] == num:
                    self.check[i][j] = True

    def bingo_count(self):
        ret = 0
        # 横方向
        for i in range(self.length):
            ok = True
            for j in range(self.length):
                if not self.check[i][j]:
                    ok = False
                    break
            if ok:
                ret += 1
        # 縦方向
        for i in range(self.length):
            ok = True
            for j in range(self.length):
                if not self.check[j][i]:
                    ok = False
                    break
            if ok:
                ret += 1
        # ななめ
        ok = True
        for i in range(self.length):
            if not self.check[i][i]:
                ok = False
                break
        if ok:
            ret += 1
        
        ok = True
        for i in range(self.length):
            if not self.check[i][-i-1]:
                ok = False
                break
        if ok:
            ret += 1
        
        return ret

def main():
    bingo = Bingo([list(map(int, input().split())) for i in range(3)])
    N = int(input())

    for _ in range(N):
        b = int(input())
        bingo.punch(b)
    
    if bingo.bingo_count() > 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
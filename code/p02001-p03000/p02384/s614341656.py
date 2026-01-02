# AOJ ITP1_11_B

# サイコロ。

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

class dice:
    def __init__(self):
        self.data = [0 for i in range(8)]
        a = intinput()
        for i in range(1, 7): self.data[i] = a[i - 1]  # 1, 2, 3, 4, 5, 6.
        for i in range(6): self.data[0] += a[i]  # 各位の和を0に。
        self.data[7] = a[0] * a[5] + a[1] * a[4] + a[2] * a[3]  # 対面同士の積の和。
        # dataの1, 2, 3, 4, 5, 6というindexが位置を示す。
        # 回転するとそれらの位置にある数が変化するイメージ。

    def d_read(self, a):
        # aはたとえば5, 1, 2, 6のような配列
        b = []
        for i in range(len(a)): b.append(self.data[a[i]])
        return b

    def d_write(self, b, c):
        # cはたとえば1, 2 ,6, 5のような配列で、そこにbの中身を落とす。
        if len(b) != len(c): return     # 要求と異なる。
        for i in range(len(b)): self.data[c[i]] = b[i]

    def roll(self, direction):
        # directionが'S', 'E', 'W', 'N'.
        # 'S', 'N'では3と4が不変。 'E'と'W'では2と5が不変。
        if direction == ' ': return
        if direction == 'S':
            self.d_write(self.d_read([5, 1, 2, 6]), [1, 2, 6, 5])
            
        elif direction == 'N':
            self.d_write(self.d_read([2, 6, 5, 1]), [1, 2, 6, 5])
            
        elif direction == 'W':
            self.d_write(self.d_read([3, 6, 4, 1]), [1, 3, 6, 4])
            
        elif direction == 'E':
            self.d_write(self.d_read([4, 1, 3, 6]), [1, 3, 6, 4])

    def get_label(self, i):  # i番の面の数を返す。
        return self.data[i]

    def get_index(self, n):  # nが書かれた面のindexを返す。
        for i in range(1, 7):
            if self.data[i] == n: return i
        return 0  # 見つからない場合。

def main():
    d = dice()
    q = int(input())
    command = ["", ' ', 'N', 'W', 'E', 'S', 'S']
    get_ans = [-1, -1, 3, 5, 2, 4]
    for i in range(q):
        x = intinput()
        a = x[0]; b = x[1]
        # aが上面、bが前面。答えるのは右側面。aとbは整数(indexではない).
        upper = d.get_index(a)
        d.roll(command[upper])  # aが上面に来るように回転。
        if upper == 6: d.roll('S')  # 6の場合はもう一回。
        front = d.get_index(b)   # 前面にくる数のindex.
        print(d.get_label(get_ans[front]))  # 答えを出力。

if __name__ == "__main__":
    main()

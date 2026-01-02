# AOJ ITP1_11_D

# サイコロ。

command = " SSESS"  # すべての面を総当たり。
check = []  # 側面チェック用。
check.append([2, 3, 5, 4])
check.append([3, 5, 4, 2])
check.append([5, 4, 2 ,3])
check.append([4, 2, 3, 5])

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
        self.data[7] = a[0] * a[5] + a[1] * a[4] + a[2] * a[3]  # 対面同士の積の和を7に。
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
        return -1  # 見つからない場合。

def side_check(d1, d2):
    # 上面と下面が合ってる場合の側面チェック。
    for i in range(4):
        j = 2
        while j < 6:
            if d2.get_label(check[0][j - 2]) != d1.get_label(check[i][j - 2]): break
            j += 1
        if j == 6: return True
    return False

def is_equal(d1, d2):
    if d1.get_label(0) != d2.get_label(0): return False
    if d1.get_label(7) != d2.get_label(7): return False
    # SSESSの順にまわしていけばすべての面が上面に来る。
    for i in range(6):
        d2.roll(command[i])  # 最初だけ何もしない。
        if d2.get_label(1) != d1.get_label(1): continue
        if d2.get_label(6) != d2.get_label(6): continue
        if side_check(d1, d2): return True
    return False

def main():
    diceset = []
    n = int(input())
    for i in range(n):
        diceset.append(dice())
    distinct = True
    for i in range(n):
        for j in range(i + 1, n):
            if is_equal(diceset[i], diceset[j]):
                distinct = False; break
    if distinct: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()

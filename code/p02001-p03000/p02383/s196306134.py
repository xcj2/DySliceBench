# AOJ ITP1_11_A

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
        if direction == 'S':
            self.d_write(self.d_read([5, 1, 2, 6]), [1, 2, 6, 5])
            
        elif direction == 'N':
            self.d_write(self.d_read([2, 6, 5, 1]), [1, 2, 6, 5])
            
        elif direction == 'W':
            self.d_write(self.d_read([3, 6, 4, 1]), [1, 3, 6, 4])
            
        elif direction == 'E':
            self.d_write(self.d_read([4, 1, 3, 6]), [1, 3, 6, 4])

    def get_upper(self):
        return self.data[1]

def main():
    d = dice()
    command = input()
    for i in range(len(command)):
        d.roll(command[i])
    print(d.get_upper())

if __name__ == "__main__":
    main()

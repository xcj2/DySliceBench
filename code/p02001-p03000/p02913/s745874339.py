def main():
    class rolling_hash():
        def __init__(self, sequence, char_list=None):
            self.sequence = sequence  # 文字列
            self.seq_size = len(self.sequence)  # 文字列の長さ
            self.mod = 2**61-1  # mod
            if char_list is None:  # 使われている文字のリスト
                self.char_list = "abcdefghijklmnopqrstuvwxyz"
            else:
                self.char_list = char_list
            self.base = len(self.char_list)+1  # 文字の種類数
            self.char_dict = {j: i+1 for i,
                              j in enumerate(self.char_list)}  # 文字と数値の対応表
            self.Hash_0start = [0]*(self.seq_size+1)  # 先頭からi-1文字目までのハッシュ値
            for i in range(self.seq_size):
                self.Hash_0start[i+1] = self.Hash_0start[i] + \
                    self.char_dict[self.sequence[i]] * \
                    pow(self.base, i, self.mod)

        def calc_hash(self, l, r):  # l文字目からr-1文字目までのハッシュ値
            return ((self.Hash_0start[r] - self.Hash_0start[l])
                    * pow(self.base, l*(self.mod-2), self.mod)) % self.mod

    n = int(input())
    s = input()
    h_s = rolling_hash(s)

    def value(num):
        h_dict = {}
        for i in range(len(s)-num+1):
            j = h_s.calc_hash(i, i+num)
            if j not in h_dict.keys():
                h_dict[j] = i
            else:
                if i-h_dict[j] >= num:
                    return True
        return False

    def b_search(a, b, value):
        while a+1 < b:
            med = (a+b)//2
            if value(med):
                a = med
            else:
                b = med-1
        if a == b:
            return a
        elif a+1 == b:
            if value(b):
                return b
            else:
                return a

    print(b_search(0, len(s), value))


main()

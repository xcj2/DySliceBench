# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0078
"""
import sys



class MagicSquare():
    def __init__(self, size):
        self.size = size
        self.data = [['@']*self.size for _ in range(self.size)]
        self.fill_data()

    def fill_data(self):
        num = 1
        x = self.size // 2
        y = x + 1
        self.data[y][x] = num

        while num < self.size**2:
            x += 1
            if x >= self.size:
                x = 0
            y += 1
            if y >= self.size:
                y = 0
            if self.data[y][x] == '@':
                num += 1
                self.data[y][x] = num
            else:
                while self.data[y][x] != '@':
                    x -= 1
                    if x < 0:
                        x = self.size - 1
                    y += 1
                    if y >= self.size:
                        y = 0
                num += 1
                self.data[y][x] = num

    def print_data(self):
        for row in self.data:
            temp = ""
            for d in row:
                temp += str(d).rjust(4)
            print(temp)
            temp = ""



def main(args):
    while True:
        size = int(input())
        if size < 3 or size%2 == 0:
            break
        ms = MagicSquare(size)
        ms.print_data()


if __name__ == '__main__':
    main(sys.argv[1:])
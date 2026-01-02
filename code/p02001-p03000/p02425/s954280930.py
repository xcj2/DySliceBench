#!/usr/bin/env python3
# ITP2_10_C: Bitset 1 - Bit Flag


class BitFlag:
    def __init__(self, size):
        self.size = size
        self.mask = ~(1 << self.size)
        self.data = 0 & (1 << self.size)

    def set(self, i):
        self.data |= (1 << i) & self.mask

    def test(self, i):
        return self.data & (1 << i) > 0

    def clear(self, i):
        self.data &= ~(1 << i) & self.mask

    def flip(self, i):
        self.data ^= (1 << i) & self.mask

    def all(self):
        return self.data == 2**self.size - 1

    def any(self):
        return not self.data == 0

    def none(self):
        return self.data == 0

    def count(self):
        return sum(1 for i in range(self.size) if self.test(i))

    def val(self):
        return self.data


def run():
    flg = BitFlag(64)
    q = int(input())
    for _ in range(q):
        cmd = input().split()

        if cmd[0] == '0':
            if flg.test(int(cmd[1])):
                print(1)
            else:
                print(0)
        elif cmd[0] == '1':
            flg.set(int(cmd[1]))
        elif cmd[0] == '2':
            flg.clear(int(cmd[1]))
        elif cmd[0] == '3':
            flg.flip(int(cmd[1]))
        elif cmd[0] == '4':
            if flg.all():
                print(1)
            else:
                print(0)
        elif cmd[0] == '5':
            if flg.any():
                print(1)
            else:
                print(0)
        elif cmd[0] == '6':
            if flg.none():
                print(1)
            else:
                print(0)
        elif cmd[0] == '7':
            print(flg.count())
        elif cmd[0] == '8':
            print(flg.val())


if __name__ == '__main__':
    run()


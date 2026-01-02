#!/usr/bin/env python3
# ITP2_10_C: Bitset 1 - Bit Flag


class BitMask:
    def __init__(self, size):
        self.size = size
        self.masks = []
        self.data = 0 & (1 << self.size)

    def add_mask(self, m):
        mask = 0 & (1 << self.size)
        for i in m:
            mask |= 1 << i
        self.masks.append(mask)

    def set(self, m):
        self.data |= self.masks[m]

    def test(self, i):
        return self.data & (1 << i) > 0

    def clear(self, m):
        self.data &= ~(self.masks[m])

    def flip(self, m):
        self.data ^= (self.masks[m])

    def all(self, m):
        return self.data & self.masks[m] == self.masks[m]

    def any(self, m):
        return not self.data & self.masks[m] == 0

    def none(self, m):
        return self.data & self.masks[m] == 0

    def count(self, m):
        def test(i):
            return data & (1 << i) > 0
        data = self.data & self.masks[m]
        return sum(1 for i in range(self.size) if test(i))

    def val(self, m):
        return self.data & self.masks[m]


def run():
    bit = BitMask(64)
    m = int(input())
    for _ in range(m):
        mask = [int(i) for i in input().split()]
        bit.add_mask(mask[1:])

    q = int(input())
    for _ in range(q):
        cmd, val = [int(i) for i in input().split()]

        if cmd == 0:
            if bit.test(val):
                print(1)
            else:
                print(0)
        elif cmd == 1:
            bit.set(val)
        elif cmd == 2:
            bit.clear(val)
        elif cmd == 3:
            bit.flip(val)
        elif cmd == 4:
            if bit.all(val):
                print(1)
            else:
                print(0)
        elif cmd == 5:
            if bit.any(val):
                print(1)
            else:
                print(0)
        elif cmd == 6:
            if bit.none(val):
                print(1)
            else:
                print(0)
        elif cmd == 7:
            print(bit.count(val))
        elif cmd == 8:
            print(bit.val(val))


if __name__ == '__main__':
    run()


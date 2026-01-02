from random import random, sample


def bis_l(a, k):
  l = 0
  r = len(a)
  while l != r:
    m = (l + r) >> 1
    if a[m] < k:
      l = m + 1
    else:
      r = m
  return l


def bis_r(a, k):
  l = 0
  r = len(a)
  while l != r:
    m = (l + r) >> 1
    if a[m] <= k:
      l = m + 1
    else:
      r = m
  return l


class TwoLayerSet:
    def __init__(self, p):
        self.top = []
        self.bottom = [[]]
        self.p = p

    def insert(self, key):
        (top, bottom) = (self.top, self.bottom)
        top_i = bis_l(top, key)
        if top_i != len(top) and key == top[top_i]:
            return False
        block = bottom[top_i]
        block_i = bis_l(block, key)
        if block_i != len(block) and key == block[block_i]:
            return False
        if random() < self.p:
            top.insert(top_i, key)
            bottom[top_i] = block[block_i:]
            bottom.insert(top_i, block[:block_i])
        else:
            block.insert(block_i, key)
        return True

    def erase(self, key):
        (top, bottom) = (self.top, self.bottom)
        top_i = bis_l(top, key)
        if top_i != len(top) and key == top[top_i]:
            top.pop(top_i)
            bottom[top_i].extend(bottom.pop(top_i+1))
            return True
        block = bottom[top_i]
        block_i = bis_l(block, key)
        if block_i != len(block) and key == block[block_i]:
            block.pop(block_i)
            return True
        return False

    def less(self, key):
        if key is None:
            return None
        top = self.top
        top_i = bis_l(top, key)
        block = self.bottom[top_i]
        block_i = bis_l(block, key)
        if block_i != 0:
            return block[block_i - 1]
        if top_i != 0:
            return top[top_i - 1]
        return None

    def less_equal(self, key):
        top = self.top
        top_i = bis_r(top, key)
        block = self.bottom[top_i]
        block_i = bis_r(block, key)
        if block_i != 0:
            return block[block_i - 1]
        if top_i != 0:
            return top[top_i - 1]
        return None

    def greater(self, key):
        if key is None:
            return None
        top = self.top
        top_i = bis_r(top, key)
        block = self.bottom[top_i]
        block_i = bis_r(block, key)
        if block_i != len(block):
            return block[block_i]
        if top_i != len(top):
            return top[top_i]
        return None

    def greater_equal(self, key):
        top = self.top
        top_i = bis_l(top, key)
        block = self.bottom[top_i]
        block_i = bis_l(block, key)
        if block_i != len(block):
            return block[block_i]
        if top_i != len(top):
            return top[top_i]
        return None


def main():
    n = int(input())
    p = list(map(int, input().split()))
    idx = [0] * n
    for i in range(0, n):
        idx[i] = i
    idx.sort(key=lambda i: - p[i])
    t = TwoLayerSet(1/100)
    t.insert(-1)
    t.insert(n)
    ans = 0
    for i in idx:
        nex = t.greater(i)
        nexnex = t.greater(nex)
        pre = t.less(i)
        prepre = t.less(pre)
        if prepre != None:
            ans += p[i] * (pre - prepre) * (nex - i)
        if nexnex != None:
            ans += p[i] * (i - pre) * (nexnex - nex)
        t.insert(i)
    print(ans)


main()

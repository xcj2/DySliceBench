#!/usr/bin/env python3
import sys
from random import randint

def main():
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())   
    
    class RollingHash:
        def __init__(self, s):
            self.s = s    # パターン探索を行われる側の文字列
            self.size = len(s)
            self.hashmod = 2 ** 64 - 1
            self.base = randint(2 ** 10, 2 ** 11)
            self.hash_list = self._make_rolling_hash_list()

        def _make_rolling_hash_list(self):
            hash_list = [0] * (self.size + 1)    # [h(s[0:0]), h(s[0:1]), h(s[0:2]), h(s[0:3]), ..., h(s[0:size])]
            prev = 0
            for i in range(1, self.size + 1):
                hash_num = (prev * self.base + ord(self.s[i-1])) % self.hashmod
                hash_list[i] = hash_num
                prev = hash_num
            return hash_list
        
        def calc_interval_hash(self, i, j):
            """
            s[i:j] のハッシュを計算
            """
            return (self.hash_list[j] - self.hash_list[i] * pow(self.base, (j - i), self.hashmod)) % self.hashmod

    
    def span_bisect(rolling):
        left = 1    # 絶対に発見成功するとわかっている
        right = (n // 2) + 1    # 絶対に発見失敗するとわかっている
        while right - left > 1:
            d = dict()
            mid_span = left + (right - left) // 2    # 二分探索で今回選ばれた span
            for i in range(n - mid_span + 1):
                j = i + mid_span
                h = rolling.calc_interval_hash(i, j)
                try:
                    first_j = d[h]
                    if first_j <= i:
                        left = mid_span
                        break
                except KeyError:
                    d[h] = j
            else:
                right = mid_span
        return left


    n = ii()
    s = input()
    if len(list(set(list(s)))) == n:
        print(0)
    else:
        # main
        rolling = RollingHash(s)
        print(span_bisect(rolling))


if __name__ == "__main__":
    main()
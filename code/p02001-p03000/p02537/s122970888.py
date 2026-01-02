#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()
# ライブラリ参照https://atcoder.jp/contests/practice2/submissions/16580070
class SegmentTree:
 
    __slots__ = ["func", "e", "original_size", "n", "data"]
 
    def __init__(self, length_or_list, func=max, e=-10**18):
        self.func = func
        self.e = e
        if isinstance(length_or_list, int):
            self.original_size = length_or_list
            self.n = 1 << ((length_or_list - 1).bit_length())
            self.data = [self.e] * (self.n*2)
        else:
            self.original_size = len(length_or_list)
            self.n = 1 << ((self.original_size - 1).bit_length())
            self.data = [self.e] * self.n + length_or_list + \
                [self.e] * (self.n - self.original_size)
            for i in range(self.n-1, 0, -1):
                self.data[i] = self.func(self.data[2*i], self.data[2*i+1])
 
    def replace(self, index, value):
        index += self.n
        self.data[index] = value
        index //= 2
        while index > 0:
            self.data[index] = self.func(
                self.data[2*index], self.data[2*index+1])
            index //= 2
 
    def folded(self, l, r):
        left_folded = self.e
        right_folded = self.e
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                left_folded = self.func(left_folded, self.data[l])
                l += 1
            if r % 2:
                r -= 1
                right_folded = self.func(self.data[r], right_folded)
            l //= 2
            r //= 2
        return self.func(left_folded, right_folded)
 
    def all_folded(self):
        return self.data[1]
 
    def __getitem__(self, index):
        return self.data[self.n + index]
 
    def max_right(self, l, f):
        # assert f(self.e)
        if l >= self.original_size:
            return self.original_size
        l += self.n
        left_folded = self.e
        while True:
            # l //= l & -l
            while l % 2 == 0:
                l //= 2
            if not f(self.func(left_folded, self.data[l])):
                while l < self.n:
                    l *= 2
                    if f(self.func(left_folded, self.data[l])):
                        left_folded = self.func(left_folded, self.data[l])
                        l += 1
                return l - self.n
            left_folded = self.func(left_folded, self.data[l])
            l += 1
            if l == l & -l:
                break
        return self.original_size
 
    # 未verify
    def min_left(self, r, f):
        # assert f(self.e)
        if r == 0:
            return 0
        r += self.n
        right_folded = self.e
        while True:
            r //= r & -r
            if not f(self.func(self.data[r], right_folded)):
                while r < self.n:
                    r = 2 * r + 1
                    if f(self.func(self.data[r], right_folded)):
                        right_folded = self.func(self.data[r], right_folded)
                        r -= 1
                return r + 1 - self.n
            if r == r & -r:
                break
        return 0

def main():
    n, k= map(int, input().split())
    A = 300010    
    st = SegmentTree(A,e=0)
    for _ in range(n):
        q = int(input())
        update=st.folded(max(0,q-k), min(300005,q+k+1))
        st.replace(q,update+1)
    print(st.all_folded())



if __name__ == '__main__':
    main()

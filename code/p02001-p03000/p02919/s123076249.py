import sys
import random
from operator import itemgetter


class RandomizedBinarySearchTree:
    def __init__(self, n):
        n += 10
        self.n = n
        self.children = [[0] * n, [0] * n]
        self.values = [0] * n
        self.counts = [0] * n
        self.indices = list(range(n - 2, -1, -1))
        self.root = -1

    def merge(self, left_root, right_root):
        children = self.children
        counts = self.counts
        li = left_root
        ri = right_root
        stack = []
        while li != -1 and ri != -1:
            if random.randrange(counts[li] + counts[ri]) < counts[li]:
                stack.append((li, 1))
                li = children[1][li]
            else:
                stack.append((ri, 0))
                ri = children[0][ri]

        i = li if li != -1 else ri
        while stack:
            pi, is_right = stack.pop()
            children[is_right][pi] = i
            counts[pi] = counts[children[0][pi]] + counts[children[1][pi]] + 1
            i = pi

        return i

    def split(self, root, x):
        i = root
        children = self.children
        values = self.values
        counts = self.counts
        l_stack = []
        r_stack = []
        while i != -1:
            if x < values[i]:
                r_stack.append(i)
                i = children[0][i]
            else:
                l_stack.append(i)
                i = children[1][i]

        li, ri = -1, -1
        while l_stack:
            pi = l_stack.pop()
            children[1][pi] = li
            counts[pi] = counts[children[0][pi]] + counts[li] + 1
            li = pi
        while r_stack:
            pi = r_stack.pop()
            children[0][pi] = ri
            counts[pi] = counts[ri] + counts[children[1][pi]] + 1
            ri = pi

        return li, ri

    def insert(self, x):
        children = self.children
        values = self.values
        counts = self.counts

        ni = self.indices.pop()
        children[0][ni] = children[1][ni] = -1
        values[ni] = x
        counts[ni] = 1

        li, ri = self.split(self.root, x)
        self.root = self.merge(self.merge(li, ni), ri)

    def delete(self, x):
        children = self.children
        counts = self.counts
        li, mri = self.split(self.root, x - 1)
        mi, ri = self.split(mri, x)

        if mi == -1:
            self.root = self.merge(li, ri)
            return

        if counts[mi] == 1:
            self.indices.append(mi)
            self.root = self.merge(li, ri)
            return

        i = mi
        stack = []
        while i != -1:
            if children[0][i] != -1 and children[1][i] != -1:
                to_right = 1 if counts[children[0][i]] < counts[children[1][i]] else 0
                stack.append((i, to_right))
                i = children[to_right][i]
            else:
                if children[0][i] != -1:
                    if stack:
                        pi, is_right = stack[-1]
                        children[is_right][pi] = children[0][i]
                    else:
                        mi = children[0][i]
                elif children[1][i] != -1:
                    if stack:
                        pi, is_right = stack[-1]
                        children[is_right][pi] = children[1][i]
                    else:
                        mi = children[1][i]
                else:
                    pi, is_right = stack[-1]
                    children[is_right][pi] = -1
                break

        self.indices.append(i)
        while stack:
            pi, _ = stack.pop()
            counts[pi] -= 1

        self.root = self.merge(self.merge(li, mi), ri)

    def upper_bound(self, x, default=-1):
        i = self.root
        children = self.children
        values = self.values
        counts = self.counts
        y = default
        c = counts[i]
        j = 0
        while i != -1:
            if x < values[i]:
                y = values[i]
                c = j + counts[children[0][i]]
                i = children[0][i]
            else:
                j += counts[children[0][i]] + 1
                i = children[1][i]
        return y, c

    def lower_bound(self, x, default=-1):
        i = self.root
        children = self.children
        values = self.values
        counts = self.counts
        y = default
        c = counts[i]
        j = 0
        while i != -1:
            if x <= values[i]:
                y = values[i]
                c = j + counts[children[0][i]]
                i = children[0][i]
            else:
                j += counts[children[0][i]] + 1
                i = children[1][i]
        return y, c

    def get_k_th(self, k, default=-1):
        i = self.root
        children = self.children
        values = self.values
        counts = self.counts
        if counts[i] <= k:
            return default
        j = k
        while i != -1:
            left_count = counts[children[0][i]]
            if left_count == j:
                return values[i]
            elif left_count > j:
                i = children[0][i]
            else:
                j -= left_count + 1
                i = children[1][i]
        return default

    def debug_print(self):
        print('Lefts ', self.children[0])
        print('Rights', self.children[1])
        print('Values', self.values)
        print('Counts', self.counts)
        self._debug_print(self.root, 0)

    def _debug_print(self, i, depth):
        if i != -1:
            self._debug_print(self.children[0][i], depth + 1)
            print('      ' * depth, self.values[i], self.counts[i])
            self._debug_print(self.children[1][i], depth + 1)


n = int(input())
ppp = list(map(int, input().split()))
pps = list(enumerate(ppp))
pps.sort(reverse=True, key=itemgetter(1))

rbst = RandomizedBinarySearchTree(n)
rbst.insert(-1)
rbst.insert(-1)
rbst.insert(n)
rbst.insert(n)

ans = 0
for i, p in pps:
    r1, j = rbst.upper_bound(i)
    r2 = rbst.get_k_th(j + 1)
    l1 = rbst.get_k_th(j - 1)
    l2 = rbst.get_k_th(j - 2)
    ans += p * ((l1 - l2) * (r1 - i) + (r2 - r1) * (i - l1))
    rbst.insert(i)
print(ans)

from sys import stdin

# Binary Indexed Tree
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)

        return res

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & (-i)

# Inversion Number
def inversion_num(A):
    count = 0
    bit = BIT(max(A))
    for j in range(len(A)):
        count += j-bit.sum(A[j])
        bit.add(A[j], 1)

    return count

n = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split()]
dic = {}
for i, a_i in enumerate(sorted(a), 1):
    dic[a_i] = i

# 数の大小関係を保つように、a_iが何番目に小さいかを表すリストに変形
a = [dic[a_i] for a_i in a]
print(inversion_num(a))


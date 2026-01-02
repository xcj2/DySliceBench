import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():

    class BinaryIndexedTree():
        def __init__(self, n):
            self.n = n
            self.bit = [0]*(n+1)

        def add(self, item, pos):
            index = pos
            while index < self.n+1:
                self.bit[index] += item
                index += index & (-index)

        def sum(self, pos):
            ret = 0
            index = pos
            while index > 0:
                ret += self.bit[index]
                index -= index & -index
            return ret

    N = int(input())
    S = list(input())
    Q = int(input())
    Query = [input().split() for _ in range(Q)] 

    pos_bit_list = [BinaryIndexedTree(len(S)) for _ in range(26)]

    for i, c in enumerate(S):
        pos_bit_list[ord(c)-ord('a')].add(1, i+1)

    for q in Query:
        if q[0] == '1':
            pos_bit_list[ord(S[int(q[1])-1])-ord('a')].add(-1, int(q[1]))
            pos_bit_list[ord(q[2])-ord('a')].add(1, int(q[1]))
            S[int(q[1])-1] = q[2]
        else:
            print(len([p for p in pos_bit_list if p.sum(int(q[2])) - p.sum(int(q[1])-1) > 0]))

if __name__ == '__main__':
    resolve()

import sys


class BinaryIndexedTree():
    '''
    1-indexed
    '''
    def __init__(self, A):
        self.__n = len(A)
        self.__node = [0] * (self.__n + 1)
        self.__data = [0] * (self.__n + 1)

        S = [0] * (self.__n + 1)
        for i in range(self.__n):
            S[i + 1] = S[i] + A[i]

        for i in range(1, self.__n + 1):
            self.__data[i] = A[i - 1]
            self.__node[i] = S[i] - S[i - (i & -i)]

    def add(self, i, v):
        self.__data[i] += v
        while i <= self.__n:
            self.__node[i] += v
            i += i & -i

    def sum(self, i):
        ''' [1, i]の和
        '''
        rst = 0
        while i > 0:
            rst += self.__node[i]
            i -= i & -i
        return rst
    
    def get(self, i, j):
        '''[i, j]の和
        '''
        if i == j:
            return self.__data[i]
        else:
            return self.sum(j) - self.sum(i - 1)


def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    P = [[] for _ in range(N)]
    for i, c in enumerate(C):
        P[c - 1].append(i)

    right = [0] * N
    for p in P:
        if len(p):
            right[p.pop()] = 1
    BIT = BinaryIndexedTree(right)

    query = [[] for _ in range(N)]
    for i, s in enumerate(sys.stdin.readlines()):
        l, r = map(int, s.split())
        query[r - 1].append((l - 1, i))

    ans = [None] * Q

    cur = N - 1
    for r, q in enumerate(reversed(query)):
        r = (N - 1) - r
        while q:
            l, i = q.pop()
            while r < cur:
                c = C[cur] - 1
                p = P[c]
                if len(p):
                    BIT.add(p.pop() + 1, 1)
                cur -= 1
            tmp = BIT.get(l + 1, r + 1)
            ans[i] = tmp

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()

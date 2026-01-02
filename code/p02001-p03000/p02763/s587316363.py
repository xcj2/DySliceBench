def main():
    N = int(input())
    S = ['$'] + list(input())

    c = lambda x: ord(x) - ord('a')
    bit = [BinaryIndexedTree(N) for _ in range(26)]
    for i, l in enumerate(S):
        if i == 0: continue
        bit[c(l)].add(i, 1)

    Q = int(input())
    for _ in range(Q):
        t, a, b = input().split()
        if t == '1':
            a = int(a)
            bit[c(S[a])].add(a, -1)
            bit[c(b)].add(a, 1)
            S[a] = b
        else:
            a, b = int(a), int(b)
            ans = 0
            for i in range(26):
                t = bit[i].sum(b)
                if a >= 1: t -= bit[i].sum(a-1)
                ans += 1 if t else 0
            print(ans)

class BinaryIndexedTree:
    def __init__(self, n=None, f=lambda x,y:x+y, zero=0, initial_values=None):
        assert(n or initial_values)
        self.__f, self.__z, = f, zero
        self.__n = n if n else len(initial_values)
        self.__dat = [zero] * (self.__n + 1)
        if initial_values:
            for i in range(1, self.__n + 1): self.add(i, initial_values[i-1]) #slow

    def add(self, i, v):
        while i <= self.__n:
            self.__dat[i] = self.__f(self.__dat[i], v)
            i += -i&i

    def sum(self, r):
        ans = self.__z
        while r:
            ans = self.__f(ans, self.__dat[r])
            r -= -r&r
        return ans

if __name__ == '__main__':
    main()

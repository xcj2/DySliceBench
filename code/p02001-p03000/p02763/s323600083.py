def main():
    import sys
    input = sys.stdin.readline

    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x):
            while i <= self.size:
                self.tree[i] += x
                i += i & -i

    N = int(input())
    S = input().rstrip('\n')
    Q = int(input())

    S = [s for s in S]

    bit = [Bit(N) for _ in range(26)]
    for i, s in enumerate(S):
        j = ord(s) - 97
        bit[j].add(i+1, 1)
    for _ in range(Q):
        flg, l, r = input().split()
        if flg == '1':
            i = int(l)
            c = r
            si = S[i-1]
            bit[ord(si)-97].add(i, -1)
            bit[ord(c)-97].add(i, 1)
            S[i-1] = c
        else:
            l = int(l)
            r = int(r)
            ans = 0
            for j in range(26):
                if bit[j].sum(r) - bit[j].sum(l-1):
                    ans += 1
            print(ans)


if __name__ == '__main__':
    main()

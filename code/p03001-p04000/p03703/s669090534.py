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


def main():
    N, K = map(int, input().split())
    ac = [0] * (N + 1)
    place = {0: 0}
    for i in range(N):
        a = int(input()) - K
        ac[i+1] = ac[i] + a * (10 ** 5) + 1
        place[ac[i+1]] = i+1
    ac.sort()
    ac_cmpr = [0] * (N+1)
    for i in range(N+1):
        ac_cmpr[place[ac[i]]] = i + 1
    bit = Bit(N+2)
    bit.add(ac_cmpr[0], 1)
    ans = 0
    for i in range(1, N+1):
        ans += bit.sum(ac_cmpr[i])
        bit.add(ac_cmpr[i], 1)

    print(ans)


if __name__=='__main__':
    main()

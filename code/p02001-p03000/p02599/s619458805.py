import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
C = list(map(int, input().split()))
LR = []
for i in range(Q):
    l, r = map(int, input().split())
    LR.append((l-1, r-1, i))


class FenwickTree(object):
    def __init__(self, n):
        self._bit = [0] * (n+1)
        self.n = n+1
    
    def add(self, i, a):
        i += 1
        while i < self.n:
            self._bit[i] += a
            i += i & -i
    
    def sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self._bit[i]
            i -= i & -i
        return ret


def solve():
    memo = [-1] * N
    ST = []
    nst = 0
    for i, c in enumerate(C[::-1]):
        if memo[c-1] >= 0:
            ST.append((N-i-1, memo[c-1]))
            nst += 1
        memo[c-1] = N-i-1
    # ST.sort(reverse=True)
    LR.sort(reverse=True, key=lambda x:x[0])
    ans =[0 for _ in range(Q)]
    ft = FenwickTree(N+1)
    j = 0
    for l, r, i in LR:
        while j < nst and ST[j][0] >= l:
            ft.add(ST[j][1], 1)
            j += 1
        ans[i] = r - l + 1 - ft.sum(r)
    return ans

if __name__ == "__main__":
    print('\n'.join(map(str, solve())))

import sys

class RMQ(): #range minimum query
    def __init__(self, N, V): #create segment tree with initial value V
        d, k = 1, 0
        while d < N:
            d <<= 1
            k += 1
        self.tree = [V for _ in range(2 * d - 1)]
        self.size = d 
    
    def update(self, i, a): #update cell i by value a
        now = self.size - 1 + i
        if self.tree[now] != a:
            self.tree[now] = a
            while now > 0:
                now = (now - 1) // 2
                self.tree[now] = self.tree[2 * now + 1] | self.tree[2 * now + 2]

    def search(self, lower, higher, lbound, hbound, pos): #search minimum value of [lower, higher) init: lbound = 0, hbound = self.size, pos = 0
        if higher <= lbound or hbound <= lower: return 0
        if lower <= lbound and hbound <= higher: return self.tree[pos]
        else:
            left = self.search(lower, higher, lbound, (lbound + hbound) // 2, 2 * pos + 1)
            right = self.search(lower, higher, (lbound + hbound) // 2, hbound, 2 * pos + 2)
            return left | right


def solve():
    input = sys.stdin.readline
    ab = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    abn = dict()
    for i, st in enumerate(ab): abn[st] = i
    N = int(input())
    S = list(input().strip("\n"))
    SegTree = RMQ(N, 0)
    for i, s in enumerate(S):
        ns = 1 << abn[s]
        SegTree.update(i, ns)
    Q = int(input())
    for _ in range(Q):
        t, l, r = input().strip("\n").split()
        if t == "1": SegTree.update(int(l) - 1, 1 << abn[r])
        elif t == "2": 
            bitans = SegTree.search(int(l) - 1, int(r), 0, SegTree.size, 0)
            ans = 0
            while bitans > 0:
                if bitans & 1 == 1: ans += 1
                bitans >>= 1
            print(ans)
    return 0

if __name__ =="__main__":
    solve()
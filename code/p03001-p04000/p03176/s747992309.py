import sys

class segTree():
    def __init__(self, N, value):
        d, k = 1, 0
        while d < N:
            d *= 2
            k += 1
        self.tree = [value for _ in range(2 * d - 1)]
        self.size = d
    
    def update(self, i, a):
        now = self.size - 1 + i 
        self.tree[now] = a
        while now > 0:
            now = (now - 1) // 2
            self.tree[now] = max(self.tree[2 * now + 1], self.tree[2 * now + 2])
        #print(self.tree)

    def search(self, lower, higher, lbound, hbound, pos):
        if higher <= lbound or hbound <= lower: return 0
        if lower <= lbound and hbound <= higher: return self.tree[pos]
        else:
            left = self.search(lower, higher, lbound, (lbound + hbound) // 2, 2 * pos + 1)
            right = self.search(lower, higher, (lbound + hbound) // 2, hbound, 2 * pos + 2)
            return max(left, right)
        
def solve():
    input = sys.stdin.readline
    N = int(input())
    H = [int(h) for h in input().split()]
    A = [int(a) for a in input().split()]
    highest = max(H) + 1
    ans = segTree(highest, 0)
    for i, h in enumerate(H): 
        maxSum = ans.search(0, h, 0, ans.size, 0)
        ans.update(h, A[i] + maxSum)
    print(ans.search(0, highest, 0, ans.size, 0))

    return 0

if __name__ == "__main__":
    solve()
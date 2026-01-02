class Max_Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def get_max(self, i=None):
        if i is None:
            i = self.size
        m = 0  # -INF
        while i > 0:
            m = max(m, self.tree[i])
            i -= i & -i
        return m

    def update(self, i, x):
        while i <= self.size:
            self.tree[i] = max(x, self.tree[i])
            i += i & -i
def main():
    N = int(input())
    *H, = map(int, input().split())
    *A, = map(int, input().split())
    
    dp = Max_Bit(N)
    sort_H_i = sorted((h, i) for i, h in enumerate(H))
    for h, i in sort_H_i:
        dp.update(i+1, dp.get_max(i) + A[i])
    print(dp.get_max())

if __name__ == '__main__':
    main()
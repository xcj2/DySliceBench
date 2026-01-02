class SegmentTree():
    def __init__(self, arr, func=min, ie=2**63):
        self.n = 2**(len(arr) - 1).bit_length()
        self.ie = ie
        self.func = func
        self.tree = [ie for _ in range(2 * self.n)]
        for i in range(len(arr)):
            self.tree[self.n + i - 1] = arr[i]
        for i in range(self.n - 1)[::-1]:
            self.tree[i] = func(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def set(self, index, x):
        index += self.n - 1
        self.tree[index] = x
        while index:
            index = (index - 1) // 2
            self.tree[index] = self.func(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def query(self, left, right):
        if right <= left:
            return self.ie
        left += self.n - 1
        right += self.n - 2
        tmp_l = self.ie
        tmp_r = self.ie
        while right - left > 1:
            if left & 1 == 0:
                tmp_l = self.func(tmp_l, self.tree[left])
            if right & 1 == 1:
                tmp_r = self.func(self.tree[right], tmp_r)
                right -= 1
            left = left // 2
            right = (right - 1) // 2
        if left == right:
            tmp_l = self.func(tmp_l, self.tree[left])
        else:
            tmp_l = self.func(self.func(tmp_l, self.tree[left]), self.tree[right])
        return self.func(tmp_l, tmp_r)

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

arr = [0 for _ in range(N + 1)]
dp = SegmentTree(arr, max, 0)

for i in range(N):
    dp.set(H[i], dp.query(0, H[i]) + A[i])

print(dp.query(0, N + 1))
n = int(input())
a = [int(x) for x in input().split()]
index = [0]*n
for i in range(n):
    index[a[i]-1] = i+2


class BIT:
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
        if i == 0:
            print("Oops! BIT is an 1-indexed tree.")
            exit()
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


ans = 0
s = BIT(n+2)
s.add(1, -1)
s.add(n+2, 1)
for i in range(n):
    s.add(index[i], 1)

    left = s.sum(index[i]) - 1
    bottom = 1
    top = index[i]
    while top - bottom > 1:
        middle = (top+bottom)//2
        if s.sum(middle) >= left:
            top = middle
        else:
            bottom = middle
    if left == -1:
        left = 1
    else:
        left = top

    right = s.sum(index[i])+1
    bottom = index[i]
    top = n+2
    while top - bottom > 1:
        middle = (top+bottom)//2
        if s.sum(middle) >= right:
            top = middle
        else:
            bottom = middle
    right = top

    ans += (i+1)*(index[i]-left)*(right-index[i])

print(ans)

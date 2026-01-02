class BIT:
    def __init__(self, n):
        #A1 ... AnのBIT(1-indexed)
        self.BIT = [0] * (n + 1)
        self.n = n

    #A1 ~ Aiまでの和 O(logN)
    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    #Ai += x O(logN)
    def add(self, idx, x):
        while idx <= self.n:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return
def get_int(f):
    if "." not in f:
        return int(f),0
    return int(f.replace(".","")),len(f)-f.index(".")-1
n = int(input())
p = []
for i in range(n):
    a, b = get_int(input())
    c, d = 0, 0
    while a % 2 == 0:
        c += 1
        a //= 2
    while a % 5 == 0:
        d += 1
        a //= 5
    c -= b
    d -= b
    p.append((c, d))
p.sort(key=lambda x:x[0])
now = n - 1
t = BIT(50)
ans = 0
for i in range(n):
    for j in range(now, i, -1):
        if p[i][0] + p[j][0] >= 0:
            t.add(-p[j][1] + 25, 1)
            now -= 1
        else:
            break
    if now < i:
        t.add(-p[i][1] + 25, -1)
    ans += max(0, t.query(25 + p[i][1]))

print(ans)
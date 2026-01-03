class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, k, x):
        k += 1
        while k <= self.n:
            self.bit[k] += x
            k += k & -k

    def sum(self, k):
        s = 0
        while k > 0:
            s += self.bit[k]
            k -= k & -k
        return s


from collections import defaultdict
N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))


B = [0]
s = 0
for i in range(N):
    B.append(s + A[i] - (i + 1) * K)
    s += A[i]

D = [0] * (N + 1)
d = defaultdict(list)
for i in range(len(B)):
    d[B[i]].append(i)

B = sorted(B)
k = 0
i = 0
while i < N + 1:
    m = len(d[B[i]])
    for l in d[B[i]]:
        D[l] = k
    k += 1
    i += m

bt = BIT(N + 1)
num = 0
for i in range(N + 1):
    num += bt.sum(D[i] + 1)
    bt.add(D[i], 1)
print(num)




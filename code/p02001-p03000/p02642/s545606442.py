from collections import Counter
import sys

def input():
    return sys.stdin.readline().strip()

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            yield i
            if i != n // i:
                yield n//i
        i += 1

n,*A = get_all_int()
A.sort()



C = dict(Counter(A))
keys = C.keys()
# log(C)

checks = [False] * (1000009)

B = []
for i,a in enumerate(A):
    if C[a] == 1:
        B.append(a)
    elif not checks[a]:
        for j in range(a, 1000009, a):
            checks[j] = True

# log(B)

ans = 0

for i,a in enumerate(B):
    if not checks[a]:
        ans += 1
        for j in range(a, 1000009, a):
            checks[j] = True

print(ans)

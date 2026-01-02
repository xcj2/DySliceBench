import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = input()
k = int(input())

def calc(i, k):
    return comb(len(n) - i - 1, k) * 9 ** k

def cnt(n):
    cnt = 0
    for c in n:
        if c != "0":
            cnt += 1
    return cnt

ans = 0
if cnt(n) == k:
    ans += 1


for i in range(len(n)):
    if int(n[i]) == 0:
        continue
    if len(n)-i > k:
        ans += calc(i, k)
    k -= 1
    if k < 0:
        break
    if len(n)-i > k:
        ans += (int(n[i]) - 1) * calc(i, k)
print(ans)

import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


def divisors(m: int):
    i = 1
    div = []
    while i * i <= m:
        if m % i == 0:
            div.append(i)
            div.append(m // i)
        i += 1

    return list(set(div))

n = ni()
a = [0] + list(li())
b = [0]*(n+1)
ans = []
for i in range(n, 0, -1):
    into = False
    if b[i] % 2 != a[i]:
        b[i] += 1
        ans.append(i)
        into = True

    if into:
        bi_div = divisors(i)

        for divi in bi_div:
            b[divi] += 1

print(len(ans))
if len(ans) > 0:
    print(*ans)

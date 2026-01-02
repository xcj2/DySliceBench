import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


s = S()
k = I()
counts = [1]
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        counts[-1] += 1
    else:
        counts.append(1)

# 文字が 1 種類
if len(counts) == 1:
    print(len(s) * k // 2)

else:
    ans = 0
    # 語頭と語尾が同じ文字でない
    if s[0] != s[-1]:
        for cnt in counts:
            ans += cnt // 2
        ans *= k

    # 語頭と語尾が同じ文字
    else:
        # 語頭と語尾(の連続する文字)を除いて考える
        for cnt in counts[1:-1]:
            ans += cnt // 2
        ans *= k
        # 一番初めの先頭の変換のぶんを足す
        ans += counts[0] // 2
        # 一番最後の末尾の変換のぶんを足す
        ans += counts[-1] // 2
        length = counts[0] + counts[-1]
        # k-1個あるsの境目の変換の回数
        ans += (length // 2) * (k - 1)

    print(ans)

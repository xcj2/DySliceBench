from collections import Counter
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')
MOD = 10 ** 9 + 7


n, k = LI()
a = LI()
c = list(Counter(sorted(a)).items())
# a 単体の中での転倒数
count_in_a = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            count_in_a += 1
# b 全体での転倒数
count_in_b = 0
# ある a の各要素の もうひとつの a の各要素に対する転倒数の数を計算
for elem_1 in a:
    for elem_2 in a:
        if elem_1 > elem_2:
            count_in_b += 1
# b に含まれる k 個の a から 2 つ転倒数を考えるペアを選ぶ(k C 2)
ans = count_in_a * k + count_in_b * (k * (k - 1) // 2)
ans %= MOD
print(ans)

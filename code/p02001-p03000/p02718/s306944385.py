import sys
stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]

n,m = MI()
a = sorted(LI())[::-1]
asum = sum(a)
if a[:m][-1]>=asum*(1/(4*m)):
    print('Yes')
else:
    print('No')
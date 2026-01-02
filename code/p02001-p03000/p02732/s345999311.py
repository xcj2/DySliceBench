import sys
stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)

def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]

n = II()
a = LI()

b = [0]*(n+1)
count = 0
for i in range(n):
    b[a[i]] += 1
for i in range(n+1):
    count += b[i]*(b[i]-1)/2
for i in a:
    print(int(count-b[i]+1))
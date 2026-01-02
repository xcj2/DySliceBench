import sys

# 入力を整数に変換して受け取る
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
# 入力全てを整数に変換したものの配列を受け取る
def LI(): return list(map(int, sys.stdin.readline().split()))
# 入力全てを整数に変換して1引いたものの配列を受け取る
def LLI(rows_number): return [LI() for _ in range(rows_number)]
# リストを改行区切りで出力する
p2D = lambda x: print(*x, sep="\n")


a,b = MI()

if a <=5:
    print(0)
elif a >=6 and a <= 12:
    print(int(b/2))
else:
    print(b)
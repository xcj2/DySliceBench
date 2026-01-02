import re  # 正規表現, findall('正規表現', 文字列), search('正規表現', 文字列)
import sys # プログラム終了：sys.exit()
# sys.setrecursionlimit(10**6) # 再帰呼び出しの上限を上げる

def i_input(): return int(input())
def s_input(): return map(int,input().split())
def l_input(): return list(map(int, input().split()))
# 文字列のまま受け取りたいときはinput()

N = i_input()
A = l_input()

alice = 0
bob = 0

for i in range(N):
    biggest = max(A)
    if i % 2 == 0:
        alice += biggest
    else:
        bob += biggest
    A.remove(biggest)

print(alice - bob)

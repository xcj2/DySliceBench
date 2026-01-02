import re  # 正規表現, findall('正規表現', 文字列), search('正規表現', 文字列)
import sys # プログラム終了：sys.exit()
# sys.setrecursionlimit(10**6) # 再帰呼び出しの上限を上げる

def i_input(): return int(input())
def s_input(): return map(int,input().split())
def l_input(): return list(map(int, input().split()))
# 文字列のまま受け取りたいときはinput()

n = i_input()
current_a_list = l_input()
count = 0

while 1:
    # print(current_a_list)
    new_a_list = []
    for a in current_a_list:
        if a % 2 == 0:
            new_a_list.append(a // 2)
        else:
            print(count)
            sys.exit()

    count += 1
    current_a_list = new_a_list
    
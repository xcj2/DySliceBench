import re  # 正規表現, findall('正規表現', 文字列), search('正規表現', 文字列)
import sys # プログラム終了：sys.exit()
# sys.setrecursionlimit(10**6) # 再帰呼び出しの上限を上げる

def i_input(): return int(input())
def s_input(): return map(int,input().split())
def l_input(): return list(map(int, input().split()))
# 文字列のまま受け取りたいときはinput()

def check(x, a, b, c):
    diff = x - 500 * a - 100 * b
    if diff >= 0 and diff % 50 == 0 and diff // 50 <= c:
        return True
    else:
        return False

def main():
    a = i_input() # 500
    b = i_input() # 100
    c = i_input() # 50
    x = i_input() # sum

    count = 0
    for i in range(a + 1):
        for j in range(b + 1):
            if check(x, i, j, c):
                count += 1

    print(count)

if __name__ == "__main__":
    main()

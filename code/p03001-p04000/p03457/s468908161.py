import re  # 正規表現, findall('正規表現', 文字列), search('正規表現', 文字列)
import sys # プログラム終了：sys.exit()
# sys.setrecursionlimit(10**6) # 再帰呼び出しの上限を上げる

def i_input(): return int(input())
def s_input(): return map(int,input().split())
def l_input(): return list(map(int, input().split()))
# 文字列のまま受け取りたいときはinput()

def main():
    N = i_input()
    T, X, Y = [], [], []
    for _ in range(N):
        t, x, y = s_input()
        T.append(t)
        X.append(x)
        Y.append(y)

    pre_t, pre_x, pre_y = 0, 0, 0
    for i in range(N):
        now_t, now_x, now_y = T[i], X[i], Y[i]
        time = now_t - pre_t
        x_diff = abs(now_x - pre_x)
        y_diff = abs(now_y - pre_y)

        if time >= x_diff + y_diff and\
            (time - x_diff - y_diff) % 2 == 0:
            pre_t, pre_x, pre_y = now_t, now_x, now_y
        else:
            print('No')
            sys.exit()
    
    print('Yes')

if __name__ == "__main__":
    main()
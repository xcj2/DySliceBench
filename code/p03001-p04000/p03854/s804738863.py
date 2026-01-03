import re  # 正規表現, findall('正規表現', 文字列), search('正規表現', 文字列)
import sys # プログラム終了：sys.exit()
# sys.setrecursionlimit(10**6) # 再帰呼び出しの上限を上げる

def i_input(): return int(input())
def s_input(): return map(int,input().split())
def l_input(): return list(map(int, input().split()))
# 文字列のまま受け取りたいときはinput()

def main():
    S = input()

    while 1:
        if S == '':
            print('YES')
            sys.exit()
        elif end_match('dreamer', S):
            S = S[:-7]
            # print('a', S)
        elif end_match('eraser', S):
            S = S[:-6]
            # print('b', S)
        elif end_match('dream', S):
            S = S[:-5]
            # print('c', S)
        elif end_match('erase', S):
            S = S[:-5]
            # print('d', S)
        else:
            print('NO')
            sys.exit()

def end_match(query, S):
    length = len(query)
    end = S[-length:]
    # print(query, end)
    if end == query:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
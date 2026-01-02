import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(n):#AtCoder Beginner Contest 101 b
    s=0
    for c in str(n):
        s=s+int(c)#'int'数値ではないものを数値にする'str'文字列じゃないものを文字列にする関数
    if n%s==0:
        return 'Yes'
    else:
        return'No'

# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line = sys.stdin.readline().rstrip()
    return int(line)

def main():
    n = readQuestion()
    answer = solve(n)
    print(answer)
    
if __name__ == '__main__':
    main()
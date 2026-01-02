import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(a,b,c):
    if len(c) == a+b+1:
        if  c.count("-")!=1:
            return "No"
        elif c[a]==("-"):
            return "Yes"
        else:
            return "No"
    else:
        return "No"
# ここから下は，入力・出力形式が同じであれば，変えなくて良い．
def readQuestion():
    line1 = sys.stdin.readline().rstrip()
    [str_n, str_i] = line1.split(' ')
    line2 = sys.stdin.readline().rstrip()
    return (int(str_n), int(str_i), line2)

def main():
    n, i, s = readQuestion()
    answer = solve(n, i, s)
    print(answer)
    
if __name__ == '__main__':
    main()
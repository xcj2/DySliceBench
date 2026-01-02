import sys

# 関数 solve は，もちろん，問題に応じて書き換える
def solve(n, i, s):
    c = 0
    for i in s:
        if i=='-':
            c+=1
    if  s[n]=='-' and c==1:
        return 'Yes'
    else:
        return 'No'

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